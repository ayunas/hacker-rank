from stack import Stack

# bracket_pairs = {
#     '{' : '}',
#     '(' : ')',
#     '[' : ']',
#     '|' : '|'
# }

opens = ['{','(','[','|']
closes = ['}',')',']','|']

def handle_pipe(p,str_arr,i,stack):
    #only do the comparison if there is data between two pipes
    #count pipes up to current pipe
    #if the count is higher than the number of pipes before the data:
        #do the match check.  otherwise, simply push the pipe to the stack.
    # print('pipe dreams', 'pipe', p)

    pipe_count = len([p for p in str_arr[:i+1] if p == '|'])
    # print('pipecount', pipe_count,'index', i,stack.data)
    pipe_stack = [b for b in stack.data if b == '|']
    # print('pipe_stack', pipe_stack)
    if len(pipe_stack):
        if pipe_count > len(pipe_stack):
            match = stack.pop()
            if match != p:
                return True
    else:
        stack.push(p)
        return False

def bracket_balance(string):
    stack = Stack()
    str_arr = [c for c in string]
    for i,s in enumerate(str_arr):
        if s == '|':
            unbalanced = handle_pipe(s,str_arr,i,stack)
            if unbalanced:
                return 'unbalanced'
        else: 
            if s in opens:
                stack.push(s)
            elif s in closes:
                match = stack.pop()
                i = closes.index(s)
                # key = [k for k in bracket_pairs if bracket_pairs[k] == s][0]
                if match != opens[i]:
                    return 'unbalanced'
                # if match != key:
                #     return 'unbalanced'

    return 'unbalanced' if len(stack.data) else 'balanced'

a = bracket_balance('[|]|') #unbal
b = bracket_balance('I (wa)n{t to buy a on}esie[…] b(u{[t] kno}w it) won’t suit me.') #bal
c = bracket_balance("{{||[]||}}") #bal
d = bracket_balance("|||hello moto|||") #bal
e = bracket_balance("[[[hello moto]]]") #bal
f = bracket_balance("foo(bar)baz") #bal
g = bracket_balance("I am happy to take your donation; any amount will be greatly appreciated.") #bal
h = bracket_balance("I (wa)n{t to buy a on}esie[…] b(u{[t] kno}w it) won’t suit me.") #bal
i = bracket_balance("This is t(he la[st random sentence I will be writing |and| I am going to stop mid-sent]") #unbal
k = bracket_balance("()[]{}{") #unbal
m = bracket_balance("He ran| |out of money, so he {| had} to stop playing | poker.") #unbal

calls = [a,b,c,d,e,f,g,h,i,k,m]

for i,c in enumerate(calls):
    print(f"{i+1}. {c}")











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