# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example: 

# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

def happy_number(num:int) -> bool:
    visited = set()
    
    while num != 1 and num not in visited:
        visited.add(num)
        print(visited)
        arr = [int(n_str) for n_str in str(num)]
        print(arr)
        squares = map(lambda n: int(n)**2,arr)
        num = sum(squares)
        print(num)
        
    
    return True if num == 1 else False
    

x = happy_number(19)
print(x)

# from functools import reduce

# def happy_numbers(num):
#     arr = [int(n) for n in str(num)]
#     # summed = reduce(lambda s,n: s+n**2,arr)
#     summed = 0
#     for n in arr:
#         summed += n**2
#     print('summed', summed)
#     count = 0

#     while summed != 1:

#         arr = [int(n) for n in str(summed)]
#         summed = 0
#         for n in arr:
#             summed += n**2
#         count += 1
#         if count > 100000:
#             return False
    
#     return True


def isHappy(n: int) -> bool:
        visited = set()
        while n != 1 and not n in visited:
            visited.add(n)
            n = sum(map(lambda x:int(x)**2, str(n)))
        return not n in visited

z = isHappy(238)
print(z)
