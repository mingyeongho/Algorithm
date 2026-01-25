from collections import deque

def find(p, x):
    if p[x] < 0:
        return x
    p[x] = find(p, p[x])
    return p[x]

def union(p, u, v):
    u = find(p, u)
    v = find(p, v)

    if u == v:
        return False
    
    if p[u] > p[v]:
        u, v = v, u
    
    if p[u] == p[v]:
        p[u] -= 1
    
    p[v] = u
    return True

def solution(n, computers):
    answer = 0
    parent = [-1] * n
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                union(parent, i, j)
                
    for p in parent:
        if p < 0:
            answer += 1
    
    return answer