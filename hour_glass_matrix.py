# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays
# Given 6x6 2D Array:

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

#16 hour glasses
#select hourglass
#calculate hour_glass sum and return the highest value

#determine hourglass
#sum hourgloass.  record entry : 1 : (elements, sum)
#shift hourglass
#... iterate until the end of the matrix.
#
import numpy, operator
from functools import reduce

def hour_glasses(mx):
    M = numpy.array(mx)
    print('Matrix: \n', M, '\n')

    sums = {}

    tr = 0
    cs = 0
    ce = 3
    mr = 1
    mc = 1
    br = 2

    while br < 6:
        while ce <= 6:
            top = M[tr,cs:ce]
            mid = M[mr,mc]
            bottom = M[br,cs:ce]
            arr = [*top,mid,*bottom]
            print(top,mid,bottom)
            hour_glass_sum = reduce(lambda s,n: s+n, arr)
            sums[mid] = hour_glass_sum
            cs += 1
            ce += 1
            mc += 1
        tr += 1
        br += 1
        mr += 1
        
        cs = 0
        ce = 3
        mc = 1

    max_hour_glass_sum = max(sums.items(),key=operator.itemgetter(1))
    return max_hour_glass_sum

def generate_matrix():
    matrix = []
    r = 0
    for _ in range(6):
        row = []
        for i in range(r,r+6):
            row.append(i)
        matrix.append(row)
        r += 6
    return matrix

M = generate_matrix()
hour_glasses(M)

