#Завдання два
from pathlib import Path

path=Path('File_02.txt')  #Шлях до хфйлу

def get_cats_info(path):              #Функція get_cats_info(path)
    with open(path,'r') as fh:        #Відкриваємо файл
        fh=fh.readlines()             #Читаємо рядки
        list=[]                    #Створюємо пустий список
        for line in fh:
            line=line.split(',')      #Розбиваємо рядки за ","
            list.append({'id':line[0],'name':line[1],'age':line[2]})  #Додаємо параметри у список
    return list
       
print(*get_cats_info(path), sep='\n')