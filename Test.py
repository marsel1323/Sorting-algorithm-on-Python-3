import os
import random
#Открываем тектовый файл Test.txt
#В цикле от 1 до 1000 создаем тысячу рандомных чисел от 1 до 100000
#Добавляем их в список
#+Записываем эти числа в файл

def rand():
    f = open('Test.txt', 'w')
    list=[]
    for i in range(1, 1000):
        i = random.randint(1, 100000)
        list.append(i)
        f.write(str(i) + ', ')
    return list

def readTest():
    f = open('Test.txt', 'r')
    for line in f:
        print(line)

    #return list

print(readTest())