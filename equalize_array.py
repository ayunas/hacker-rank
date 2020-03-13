#camel cased because hacker rank set up that way for python.
#find min # of deletions to have an array with all the same elements

#find elemeent with most # of repeats.
#delete the rest
import operator

def equalizeArray(arr):
    repeats = {}
    for n in arr:
        dups = arr.count(n)
        repeats[n] = dups
    
    mc = max(repeats.items(),key=operator.itemgetter(1))  #mc = most common
    deletes = [n for n in arr if n != mc[0]]
    return len(deletes)


arr = [2,2,2,2,7,3]
d = equalizeArray(arr)





