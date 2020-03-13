def one_diff(nums):
    s = sorted(set(nums))  #list of unique nums in sorted order
    v = [nums.count(s[i]) + nums.count(s[i]+1) for i in range(len(s))]
    #for every element in the sorted & setted array, count the number of repeating elements and add it to the number of the repeating elements + 1.  only repeating with the repeating + 1 will satisfy condition of all the elmeents in the array to be <= 1.  return the max occurences
    return max(v)

nums = [12,4,1,3,4,5,5,5,8,10,10,10]
z = one_diff(nums)
print(z)











# def one_diff(n,nums):
#     #check diff of every value. if <= 1, push to less_ones array.
#     #return length of less_ones array
#     less_ones = []
#     for f in nums:
#         for s in nums:
#             # print(abs(f-s))
#             if f == s:
#                 continue
#             else:
#                 if (abs(f-s) <= 1):
#                     less_ones.append(f)
#                     less_ones.append(s)
#                     # less_ones.add(s)
#     print(less_ones)
#     return len(less_ones)

# nums = [1,2,4,8,10,11,12,13,14,18,22,25,12]
# x = one_diff(len(nums),nums)
# print(x)

# 

# x=sorted(set(a))
# return  max([a.count(x[i])+a.count(x[i]+1) for i in range(len(x))]+[2])

# nums = [12,4,1,3,4,5,5,5,8,10,10,10]
# pn = pick_nums(len(nums),nums)
# print(pn)

# arr = [1,2,3]
# range(len(arr))