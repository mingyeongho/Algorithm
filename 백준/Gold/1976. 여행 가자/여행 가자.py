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


N = int(input().strip())
M = int(input().strip())

p = [-1] * (N+1)
for i in range(1, N+1):
    A = [0] + list(map(int, input().split()))
    for j in range(1, len(A)):
        if A[j] == 1:
            union(i, j)

S = list(map(int, input().split()))
root = find(S[0])
for i in range(1, len(S)):
    r = find(S[i])
    if r != root:
        print("NO")
        exit(0)
print("YES")
