#Гномья сортировка в Python3
#Gnome sort in Python3

import time
begin_time = time.time()
B = ['f', 'c', 'e', 'd', 'b', 'a', 'f', 'c', 'e', 'd', 'b', 'a', 'f', 'c', 'e', 'd', 'b', 'a', 'f', 'c', 'e', 'd', 'b',
     'a', 'f', 'c', 'e', 'd', 'b', 'a', 'f', 'c', 'e', 'd', 'b', 'a', 'f', 'c', 'e', 'd', 'b', 'a', 'f', 'c', 'e', 'd',
     'b',
     'a', 'f', 'c', 'e', 'd', 'b', 'a', 'f', 'c', 'e', 'd', 'b', 'a', 'f', 'c', 'e', 'd', 'b', 'a', 'f', 'c', 'e', 'd',
     'b',
     'a', 'f', 'c', 'e', 'd', 'b', 'a', 'f', 'c', 'e', 'd', 'b', 'a', 'f', 'c', 'e', 'd', 'b', 'a', '1', '3', '2', '5',
     '8',
     '6', '7', '9']
def gnomeSort(List):
    i=1
    while i<len(List):
        if not i or List[i-1]<=List[i]:
            i+=1
        else:
            List[i], List[i-1]=List[i-1],List[i]
            i-=1
    return List

print(gnomeSort(B))
end_time = time.time()
print(end_time-begin_time)