import random

def random_counts(n):

    counts = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}

    nums = [random.randint(1,10) for i in range(0,n)]

    for n in nums:
        counts[n] += 1
    print(counts)
    return counts


random_counts(40)
random_counts(100)
random_counts(1000)
random_counts(10000)
random_counts(1000000)
random_counts(10000000)


