#Version 1
# table =  { ')': '(', ']':'[', '}':'{' }

# for _ in range(int(input())):
#     stack = []
#     for x in input():
#         if stack and table.get(x) == stack[-1]:
#             stack.pop()
#         else:
#             stack.append(x)
#     print("NO" if stack else "YES")

#Version 2
# def check_str(string):
#     stack = []
#     table = {
#         ")": "(",
#         "}": "{",
#         "]": "[",
#     }
#     for char in string:
#         if not stack:
#             stack.append(char)
#         elif char not in table:
#             stack.append(char)
#         elif table[char] == stack[-1]:
#             stack.pop()
#         else:
#             stack.append(char)
#     if stack:
#         print("NO")
#     else:
#         print("YES")    

# N = int(input().strip())
# for i in range(N):
#     check_str(input())

#Version 3 Python 2
# lefts = '{[('
# rights = '}])'
# closes = { a:b for a,b in zip(rights,lefts)}

# def valid(s):
#     stack = []
#     for c in s:
#         if c in lefts:
#             stack.append(c)
#         elif c in rights:
#             if not stack or stack.pop() != closes[c]:
#                 return False
#     return not stack  # stack must be empty at the end

# t = int(raw_input().strip())
# for a0 in xrange(t):    
#     s = raw_input().strip()    
#     if valid(s):
#         print 'YES'
#     else:
#         print 'NO'