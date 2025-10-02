import sys
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

p = [-1] * N
answer = 0
flag = True
for i in range(M):
    u, v = map(int, input().split())
    if find(u) == find(v) and flag:
        answer = i+1
        flag = False
    union(u, v)

print(answer)
