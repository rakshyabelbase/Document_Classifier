import os
import shutil


# current_path = os.getcwd()
# os.mkdir('AI')
# os.mkdir('WEB')
# print(current_path)


path = 'E:\data mining\lab\database'

# print(os.listdir(path)) #for listing the file in the given path


for file in os.listdir(path):
    # print(file) #for printing the files in the path
    if file.endswith('_AI.pdf'):
        # print(file)
        shutil.copy(path+'\\'+file, 'AI/'+file)
    elif file.endswith('_WEB.pdf'):
        shutil.copy(path+'\\'+file, 'WEB/'+file)
        # print('\n web file')
        # print(file)