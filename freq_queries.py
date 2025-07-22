from collections import defaultdict

def freq_query(queries):
    # freq = defaultdict(int)
    # counter = defaultdict(int)
    freq = {}
    counter = {}
    res = []
    for op, val in queries:
        if op == 1:
            if val in freq and freq[val] in counter:
                counter[freq[val]] -= 1
            freq[val]  = freq.get(val, 0) + 1
            counter[freq[val]] = counter.get(freq[val], 0) +1
        elif op == 2:
            if val in freq and freq[val] > 0 and freq[val] in counter:
                counter[freq[val]] -= 1
                freq[val] -= 1
                counter[freq[val]] = counter.get(freq[val], 0) + 1
        elif op == 3:

            res.append(1 if counter.get(val,0) > 0 else 0)

    return res

# print(freq_query([[1,5],[1,6],[3,1]]))

print(freq_query([(1, 5), (1, 6), (3, 2), (1, 10), (1, 10), (1, 6), (2, 5), (3, 2)]))


    # freq_query({{1,5},
    # {1,6},
    #  {3,1}

    # })
            



