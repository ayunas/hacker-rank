#for every element in the rotations array, rotate the main array by that # of elements.  store the index of the largest value into the highs array.
#


def getMaxElementIndexes(arr, rotations):
    highs = []

    for r in rotations:
        array = arr.copy()
        print('array prerotate', array,r)
        for _ in range(r):
            rotate_one(array)
        # array = rotater(array,r)
        print('array after rotation', array)
        m = max(array)
        i = array.index(m)
        # print(m,'index', i)
        highs.append(i)    
    return highs

def rotate_one(arr):
    # popped = arr.pop(0)
    # arr.append(popped)
    arr = arr[1:] + [arr[0]]

def rotater(arr,r):
    temp = arr[:r]
    rotated = arr[r:] + temp
    return rotated


arr = [1,2,3,4,5,6,7,8]
rotates = [2,3,4]

h = getMaxElementIndexes(arr,rotates)
print(h)
