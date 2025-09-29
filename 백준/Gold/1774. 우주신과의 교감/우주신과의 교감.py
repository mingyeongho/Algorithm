import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
gods = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]


def find(x):
    if p[x] < 0:
        return x
    p[x] = find(p[x])
    return p[x]


def union(u, v):
    u, v = find(u), find(v)
    if u == v:
        return False

    if p[u] > p[v]:
        u, v = v, u

    if p[u] == p[v]:
        p[u] -= 1

    p[v] = u
    return True


p = [-1] * (N+1)
for _ in range(M):
    A, B = map(int, input().split())
    union(A, B)

# 가능한 모든 간선의 거리 정보
edges = []
for i in range(1, N+1):
    xi, yi = gods[i]
    for j in range(i+1, N+1):
        xj, yj = gods[j]
        dx = xi - xj
        dy = yi - yj
        dist = math.sqrt(dx**2 + dy**2)
        edges.append((dist, i, j))

edges.sort()

answer = 0.0
for dist, u, v in edges:
    if find(u) == find(v):
        continue
    union(u, v)
    answer += dist

print(f"{answer:.2f}")
