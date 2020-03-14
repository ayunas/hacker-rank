import json,time
queries = []

with open('input008.txt','r') as f:
    freqs = []
    for l in f:
        a,b = l.split(' ')
        queries.append([int(a),int(b.strip())])

with open('input.json', 'w') as i:
    json.dump(queries,i)

def add(val,vals):
    # arr.append(val)
    if val not in vals:
        vals[val] = 1
    else:
        vals[val] += 1

def minus(val,vals):
    if val in vals:
        if vals[val] == 0:
            return
        vals[val] -= 1

    # if val in arr:
    #     arr.remove(val)

def check(freq,vals):
    # print('in check', 'frequency:', freq,'vals:', vals)
    # freq_check = [(k,v) for (k,v) in vals.items() if v == freq]
    freq_check = [*filter(lambda v: v == freq, vals.values())]
    # print('frequency found in vals?', freq_check)
    if freq_check:
        # t = freq_check[0]
        # print(f"counts of {t[0]}", t[1])
        return 1
    else:
        return 0
    # for n in arr:
    #     f = arr.count(n)
    #     print(f"counts of {n}", f)
    #     if f == freq: 
    #         return 1
    # return 0

def frequencyQueries(queries):
    vals = {}
    output = []
    # print(queries)
    ops = {1: add, 2: minus, 3: check}
    for q in queries:
        # print(q[0],ops)
        r_val = ops[q[0]](q[1],vals)
        # print(f'return value from op {q[0]}', r_val)
        if r_val == 0 or r_val == 1:
            output.append(r_val)
    return output

# queries = [[1,1],[2,2],[1,2],[1,2],[3,2],[1,1],[1,1],[2,1],[2,2],[2,2],[2,1],[3,2]]


start = time.time()
x = frequencyQueries(queries)
print(x[:30])
end = time.time()
print('execution time: ', end - start)