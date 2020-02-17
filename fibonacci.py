

# def fibonacci(n,vals=set()):
#     if n < 2:
#         return 1
#     vals.add(n)
#     print(vals)
#     return fibonacci(n-2,vals) + fibonacci(n-1,vals)

def fibonacci(n):
    if n == 1:
        return [0]
    i = 2
    seq = [0,1]
    while i < n:
        summed = seq[i-2] + seq[i-1]
        seq.append(summed)
        i += 1
    return seq

print(fibonacci(9))
