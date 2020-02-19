import random

def shuffle_list(l):
    for i in range(len(l)):
        rand_i = random.randint(i,len(l) - 1)
        l[rand_i],l[i] = l[i],l[rand_i]
    return l


shuffled = shuffle_list([1,2,3,4,5,6,7,8,9,10])
print(shuffled)

'''
The Fisher-Yates shuffle.

Here's the basic algorithm:
Begin with a list of N elements
Swap the first element with the i-th element, where i is a random position.
Repeat this for each element, in order, until you reach the end of the list.
https://github.com/LambdaSchool/Graphs/tree/master/objectives/randomness

