#https://www.hackerrank.com/challenges/introduction-to-regex/problem

#detect a floating point number using regex
#first character [+-]?
#1 decimal value : \.\d+
#


import re,sys


def find_floats():
    for num_str in sys.stdin: #input()
        regex = r'[+-]?[0-9]*\.+[0-9]*'
        match = re.match(regex,num_str)
        print(bool(match))


x = find_floats()






