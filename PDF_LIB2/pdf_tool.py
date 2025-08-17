import pdfplumber
import os

def Text_converter():
    User_inp=input('press Y to use ')
    while User_inp:
# pdf to word.txt converter
        pdfs=[]
        n=int(input('enter the number of PDFs you want to work on'))
        for i in range(n):
            name=input(f'enter the pdf no.{i+1} ')
            pdfs.append(name)
        for pdf in pdfs:
            with pdfplumber.open(pdf) as temp:
                text_content=""
                for page in temp.pages:
                    text_content+=page.extract_text() or '' #ye short circuit he JS ka ki agar phla true hua means agar text hua pdf ke uss page me to wo text extract krke de dega varna or hone ke karan jab empty page aayega to "" dega in place of None taki code loop break na ho
            with open(f'word_{os.path.splitext(pdf)[0]}.txt','w',encoding='utf-8') as f:
                f.write(text_content)
        print('your pdf to text conversion is done')
        User_inp2=input('type exit to quit').lower()
        if User_inp2=='exit':
            break    

Text_converter()