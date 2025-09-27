import sys
from collections import defaultdict
input = sys.stdin.readline


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


N, M = map(int, input().split())
edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))
edges.sort()

answer = 0
mx_cost = 0
p = [-1] * (N+1)
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c
        mx_cost = c
print(answer - mx_cost)
