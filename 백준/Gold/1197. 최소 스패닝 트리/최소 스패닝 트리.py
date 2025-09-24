import sys
input = sys.stdin.readline

V, E = map(int, input().split())
edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))
edges.sort()

parents = [-1] * (V+1)


def find(x):
    if parents[x] < 0:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(u, v):
    u, v = find(u), find(v)
    if u == v:
        return False

    if parents[v] < parents[u]:
        u, v = v, u

    if parents[u] == parents[v]:
        parents[u] -= 1

    parents[v] = u
    return True


cnt = 0
for i in range(E):
    cost, a, b = edges[i]
    if find(a) != find(b):
        union(a, b)
        cnt += cost
print(cnt)
