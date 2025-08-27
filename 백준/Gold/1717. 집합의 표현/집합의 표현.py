import sys
input = sys.stdin.readline

N, M = map(int, input().split())

P = [-1] * (N+1)


def find(x):
    if P[x] < 0:
        return x
    P[x] = find(P[x])  # 경로 압축
    return P[x]


def uni(u, v):
    u, v = find(u), find(v)
    if u == v:
        return False
    if P[v] < P[u]:  # Union by rank
        u, v = v, u
    if P[u] == P[v]:
        P[u] -= 1
    P[v] = u
    return True


for _ in range(M):
    cmd, a, b = map(int, input().split())
    if cmd == 0:  # 합연산
        uni(a, b)
    else:  # 두 원소가 같은 집합에 포함되어 있는지 확인하는 연산
        print("YES" if find(a) == find(b) else "NO")
