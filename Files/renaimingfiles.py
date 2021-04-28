import os, re

amercianDates = []
print(os.getcwd())

for filename in os.listdir(os.getcwd()):
    x = re.compile(r'(\d{1,2})-(\d{1,2})-(\d{4})')
    mo = x.sub(r'\2-\1-\3', filename)
    os.rename(os.path.join(os.getcwd(), filename), os.path.join(os.getcwd(), mo))
    print(mo)


