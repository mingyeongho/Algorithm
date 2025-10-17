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
    if p[v] == p[u]:
        p[u] -= 1
    p[v] = u
    return True


N, M = map(int, input().split())
p = [-1] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)
d = [False] * (N+1)
answer = 0
for i in range(1, N+1):
    root = find(i)
    if not d[root]:
        answer += 1
        d[root] = True
print(answer)
