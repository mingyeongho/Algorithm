from collections import defaultdict

def solution(clothes):
    d = defaultdict(list)
    for (label, kind) in clothes:
        d[kind].append(label)
    
    count = 1
    for key in d:
        count *= len(d[key]) + 1
    return count-1