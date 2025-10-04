import sys
input = sys.stdin.readline

MAX_ID = 1_000_000


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
    count[u] += count[v]
    return True


def getCount(x):
    return count[x]


N = int(input().strip())

p = [-1] * (MAX_ID+1)
count = [1] * (MAX_ID+1)
for _ in range(N):
    cmd = input().split()
    if cmd[0] == "I":
        u, v = int(cmd[1]), int(cmd[2])
        union(u, v)
    else:
        root = find(int(cmd[1]))
        cnt = getCount(root)
        print(cnt)
