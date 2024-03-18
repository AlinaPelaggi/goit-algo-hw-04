#Перше завдання
from pathlib import Path

path=Path('File_01.txt')                #Шлях до файлу  
def total_salary(path):               
    with open(path, 'r') as fh:         #Відкриваємо файл для читання
        fh=fh.readlines()             
        outlist=[]                    
    for line in fh:                     #Розбиваємо рядки за ","
        line=line.split(",")          
        outlist.append(float(line[1]))  #Переводимо з/п у число
    total=sum(outlist)                  #Рахує загальну суму
    averrage=total/len(outlist)         #Рахує середнб з/п
    return total,averrage

try:
    total,averrage=total_salary(path)
    print(f'total:{total}, averrage:{averrage}')   
except Exception as e:
    print(e)