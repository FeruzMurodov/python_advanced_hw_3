from itertools import count
from random import random, randrange

list = []
for i in range(0, 20):
    list.append(randrange(0,10))
print(list)

unique_list = set(list)
print(unique_list)
result = []
for item in unique_list:
    count = 0
    for number in list:
        if item == number:
            count +=1
    if count == 2:
        result.append(item)
print(result)