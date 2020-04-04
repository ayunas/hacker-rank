import time
from itertools import repeat
from random import randint

start = time.time()
#count = O(n).  
#solution is O(n**2) complexity
#get it down to Big O(n)
def single_number(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x           
    return None

def single_number_hashmap(arr):
    values = {}
    for x in arr:
        if x not in values:
            values[x] = 1
        else:
            values[x] += 1
    
    v,*rest = [v for (v,c) in values.items() if c == 1]
    return v

x = list(repeat(10,2000000))
x.append(11)
#execution time =  215.63181900978088 for input 2000000

s = single_number_hashmap(x)
print(s)
#execution time =  0.40767693519592285 for input 2000000

end = time.time()
print('execution time = ', end - start)

