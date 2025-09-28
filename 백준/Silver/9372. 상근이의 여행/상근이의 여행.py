import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input().strip())


def find(x):
    if p[x] < 0:
        return x
    p[x] = find(p[x])
    return p[x]


def union(u, v):
    u, v = find(u), find(v)
    if u == v:
        return False

    if p[v] < p[u]:
        u, v = v, u

    if p[u] == p[v]:
        p[u] -= 1

    p[v] = u
    return True


for _ in range(T):
    N, M = map(int, input().split())
    tree = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    p = [-1] * (N+1)
    count = 0
    for i in range(1, N+1):
        for end in tree[i]:
            if find(i) != find(end):
                union(i, end)
                count += 1
    print(count)
