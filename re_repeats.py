#https://www.hackerrank.com/challenges/re-group-groups/problem
#You are given a string. Your task is to find the first occurrence of an alphanumeric character in the string (read from left to right) that has consecutive repetitions.

import re

def re_repeats(string):
    x = re.split('\s',string)  #split string into array at any whitespace char
    squished = ''.join(x)
    regex = r'([a-zA-Z0-9])\1'  #\1 backreferencing 1st capture group. any alphanumeric char
    # regex = r'(\w)\1'  #does not pass all the tests
    m = re.findall(regex,squished)
    print(m[0]) if len(m) else print(-1)

re_repeats('asdfff')


