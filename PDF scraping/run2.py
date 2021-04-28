import pdfplumber

with pdfplumber.open('list-current-precedents.pdf') as pdf:
    pages = pdf.pages

    for page in pdf.pages:
        print(page.extract_text())
        break;

