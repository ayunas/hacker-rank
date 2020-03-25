#https://www.hackerrank.com/challenges/re-split/problem

import re

def re_split(string):
    regex = r'[,.]'
    x = re.split(regex,string)
    print(x)


re_split("1,000,000,000.00")

