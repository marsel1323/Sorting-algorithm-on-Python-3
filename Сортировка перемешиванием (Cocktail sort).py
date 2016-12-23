#Сортировка перемешиванием в Python3
#Cocktail sort in Python3

import time
begin_time = time.time()

sample = ['e', 'd', 'b', 'c', 'a']
sample1 = [0, -1, 5, -2, 3]

def cocktailSort(List):
    left = 0
    right = len(sample) - 1
    while left<=right:
        for i in range(left,right,+1):
            if sample[i]>sample[i+1]:
                sample[i], sample[i+1]=sample[i+1],sample[i]
        right -= 1

        for i in range(right, left, -1):
            if sample[i-1]>sample[i]:
                sample[i], sample[i-1]=sample[i-1],sample[i]
        left += 1
    return(List)

print(cocktailSort(sample))

end_time = time.time()
print(end_time-begin_time)