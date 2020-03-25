'''
Given an array of integers, write a function that determines whether the array contains any duplicates. Your function should return true if any element appears at least twice in the array, and it should return false if every element is distinct.
'''

#add every element into a set.  
#if the the element is in the set return true
#else add the element to the set and continue iterating

from random import randint

def contains_duplicates(nums):
    print(nums)
    numbers = set()
    for n in nums:
        if n in numbers:
            return True
        else:
            numbers.add(n)
    return False

numbys = [randint(0,100) for n in range(10)]
nums = [2,4,3,4,4,4,2,1]
x = contains_duplicates(numbys)
print(x)
