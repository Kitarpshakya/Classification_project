import fitz
import os
import pandas as pd

def get_path():
    final_path=[]
    path1= input('Enter the path for AI file: ')
    print('Path registered Successed')
    path2= input('Enter the path for WEB files: ')
    print('Path registered Successed')
    final_path.append(path1)
    final_path.append(path2)
    return final_path

def get_final_dataframe(path,flag):
    df = pd.DataFrame(columns=['Text','Label'])
    content=[]
    for file in os.listdir(path):
        if file.endswith('.pdf'):
            doc = fitz.open(path+'/'+file)
            content_temp = ''
            for page in range(len(doc)):
                content_temp = content_temp + doc[page].get_text()
            content.append(content_temp)
    df['Text'] = content
    df['Label'] = flag
    return df

def get_content_of_pdfs(file_path):
    # print('h')
    for path in file_path:    
        if '\\AI' in path:
            df_ai = get_final_dataframe(path,1)
            # print(path)
        elif '\\WEB' in path:
            df_web = get_final_dataframe(path,0)
            # print(path)
    df = df_ai.concat(df_web)
    return df
           
def get_content(file_path):
    df = pd.DataFrame(columns=['Text','Label'])
    # print('hi')
    df = get_content_of_pdfs(file_path)
    return df

def dataset_generate():
    file_path=get_path()
    dataset = get_content(file_path)
    dataset.to_csv('dataset.csv')
    # print(file_path)

if __name__=='__main__':
    dataset_generate()