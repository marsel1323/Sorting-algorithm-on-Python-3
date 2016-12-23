#Сортировка пузырьком в Python3
#Bubble sort in Python3

import time

begin_time=time.time()

def bubbleSort(List):
    for i in range(0, len(List) - 1):
        for j in range(0, len(List) - 1 - i):
            if List[j] > List[j + 1]:
                List[j], List[j + 1] = List[j + 1], List[j]
    return List

A = [1, 3, 2, 10, 5, 8, 6, 7, 9]
B = ['f', 'c', 'e', 'd', 'b', 'a','f', 'c', 'e', 'd', 'b', 'a','f', 'c', 'e', 'd', 'b', 'a','f', 'c', 'e', 'd', 'b',
     'a','f', 'c', 'e', 'd', 'b', 'a','f', 'c', 'e', 'd', 'b', 'a','f', 'c', 'e', 'd', 'b', 'a','f', 'c', 'e', 'd', 'b',
     'a','f', 'c', 'e', 'd', 'b', 'a','f', 'c', 'e', 'd', 'b', 'a','f', 'c', 'e', 'd', 'b', 'a','f', 'c', 'e', 'd', 'b',
     'a','f', 'c', 'e', 'd', 'b', 'a','f', 'c', 'e', 'd', 'b', 'a','f', 'c', 'e', 'd', 'b', 'a', '1', '3', '2', '5', '8',
     '6', '7', '9']

print(bubbleSort(B))

end_time = time.time()
print(end_time-begin_time)