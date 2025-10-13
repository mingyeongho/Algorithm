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
T = list(map(int, input().split()))
p = [-1] * (N+1)
for i in T[1:]:
    p[i] = 0

parties = []
for _ in range(M):
    P = list(map(int, input().split()))
    party = P[1:]
    init = party[0]
    for i in range(1, len(party)):
        union(init, party[i])
    parties.append(party)

answer = 0
for party in parties:
    flag = False
    for i in party:
        if find(i) == find(0):
            flag = True
            break
    if not flag:
        answer += 1
print(answer)
