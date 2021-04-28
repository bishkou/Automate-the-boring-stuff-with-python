

import fitz
import re ,os
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def get_text(filepath: str) -> str:
    with fitz.open(filepath) as doc:
        text = ""
        try :
            os.mkdir('sections')
        except:
            pass
        for page in doc:
            if page.getText().strip()[0:7] == 'Section' :
                pattern = re.compile(r'Section [A-Z]+ - (.*?)\n')
                title = re.search(pattern,text).group(1)
                with open(f'sections/{title}.txt', 'w' , encoding='utf-8') as f:
                    f.write(text)
                text=""
            text += page.getText().strip()

        title = re.search(pattern,text).group(1)
        with open(f'sections/{title}.txt', 'w' , encoding='utf-8') as f:
            f.write(text)  
        
get_text("list-current-precedents.pdf")

# with open('output.txt' , 'w' , encoding='utf-8') as f:
#     f.write(text)

def extract(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()

    pattern = re.compile(r'Section [A-Z]+ - (.*?)\n')
    section = re.search(pattern,data).group(1)



    def chapters(data):

        chapters=[]    
        # pattern = re.compile(r'(\n|Page \d{1,3} of \d{1,3})Chapter (\d{1,3})( \n| )(.*?)\d{8}',re.DOTALL)
        pattern = re.compile(r'(\n|Page \d{1,3} of \d{1,3})Chapter (\d{1,3})',re.DOTALL)
        for item in re.finditer(pattern,data):
            chapters.append([item.start(),item.end(),item.group(2)])

        for i in range(len(chapters)):
            pattern = re.compile(r'Description: ?(.*?)(Status: |Date: |\d{8}|Reason: |Instrument: )',re.DOTALL)
            if i == len(chapters)-1:
                number = len(re.findall(pattern,data[chapters[i][1]:]))
                chapters[i].append(number)
            else:
                number = len(re.findall(pattern,data[chapters[i][1]:chapters[i+1][0]]))
                chapters[i].append(number)
        
        return chapters

    chapters = chapters(data)

    #Status
    status = []
    pattern = re.compile(r'Status: \n(.*?)(\n|Date)')
    for item in re.finditer(pattern,data):
        status.append(item.group(1))


    #Heading
    pattern = re.compile(r'Heading: (.*)')
    headings = re.findall(pattern,data)

    # description
    descriptions = []
    pattern = re.compile(r'Description: ?(.*?)(Status: |Date: |\d{8}|Reason: |Instrument: )',re.DOTALL)
    for item in re.finditer(pattern,data):
        descriptions.append(item.group(1).replace('\n',' '))

    # Reason
    reasons = []
    pattern = re.compile(r'Reason: ?(.*?)(End of Chapter|\nSection|\d{8}|Status:|Date)',re.DOTALL)
    for item in re.finditer(pattern,data):
        reasons.append(item.group(1).replace('\n',' '))

    #Date
    dates = []
    pattern = re.compile('\nDate: \n(.*)(\nStatus|)')
    for item in re.finditer(pattern,data):
        dates.append(item.group(1))

    #id
    ids = []
    pattern = re.compile(r'(|\n|/\d{4}|Page \d{1,3} of \d{3})(\d{8})(.*?)Heading:',re.DOTALL)
    for item in re.finditer(pattern,data):
        ids.append(item.group(2))

    #change_dates
    change_dates = []
    pattern = re.compile(r'Change_Date:( \n|\n|)(.*?)( \n|\d{8}|)(Reason|Description|Status|\d{8})')
    for item in re.finditer(pattern,data):
        change_dates.append(item.group(2))

    # print('dates ',len(dates))
    # print('change_date ', len(change_dates))
    # print('descriptions ', len(descriptions))
    # print('reasons ', len(reasons))
    # print('status ', len(status))
    # print('ids ', len(ids))
    # print('headings ', len(headings))
    # print(chapters)

    
    df = pd.DataFrame(np.column_stack([ids,headings,dates,change_dates,status,descriptions,reasons]), 
                                columns=['ids' , 'headings', 'dates' , 'change_date' , 'status' , 'description' , 'reason'])

    # chapter to column
    df['chapter'] = '0'
    i = 0
    for j in chapters:
        for k in range(j[-1]):
            df['chapter'][i] = j[2]
            i +=1 



    df['section'] = section
    # df.loc[df['description']==' ']['description'] = 'NaN'
    # df['description'].fillna(df['reason'])
    # print(df[df['description']==' '][['reason','description']])
    for index in range(df.shape[0]):
        if df['description'][index] == ' ':
            df['description'][index] = df['reason'][index]

    df['international_coco'] = df['reason'].str.contains('COCO')
    df['has_cas'] = df['description'].str.contains('CAS number')
    df['has_uns'] = df['description'].str.contains('UN number')
    df['has_synonyms'] = df['description'].str.contains('Synonyms')
    df['country'] = 'AU'

    df['tarif_item'] = ''
    pattern = re.compile(r' \d{4}\.|\d{4}\.\d{2}\.\d{2}| \d{4},| \d{4}\)| \d{4} ')
    for index in range(df.shape[0]):
        tt = df['reason'][index]
        try:
            df['tarif_item'][index] = re.search(pattern,tt).group(0)
        except :
            df['tarif_item'][index] = ''

    df['has_tarif'] = df['reason'].str.contains(r' \d{4}\.|\d{4}\.\d{2}\.\d{2}| \d{4},| \d{4}\)| \d{4} ')

    return df

dataframes = []
for item in os.listdir('sections/'):
    
    dataframes.append(extract('sections/'+item))

res = pd.concat(dataframes)

res.to_excel('final_resulst.xlsx',index=False)

# print(extract('sections/MISCELLANEOUS MANUFACTURED ARTICLES.txt'))

# print(res['reason'].str.contains(r'\d{4}\.'))