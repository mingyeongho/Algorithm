import sys
input = sys.stdin.readline

T = int(input().strip())


def find(p: list[int], x: int) -> int:
    if p[x] < 0:
        return x
    p[x] = find(p, p[x])
    return p[x]


def uni(p: list[int], u: int, v: int) -> bool:
    u, v = find(p, u), find(p, v)
    if u == v:
        return False
    if p[v] < p[u]:
        u, v = v, u
    if p[u] == p[v]:
        p[u] -= 1
    p[v] = u
    return True


for t in range(1, T+1):
    n = int(input().strip())  # 유저의 수
    k = int(input().strip())  # 친구 관계의 수
    p = [-1] * (n+1)

    for _ in range(k):
        a, b = map(int, input().split())  # 친구 관계
        uni(p, a, b)

    m = int(input().strip())  # 미리 구할 쌍의 수
    print(f"Scenario {t}:")
    for _ in range(m):
        u, v = map(int, input().split())  # 구해야하는 쌍
        print(1 if find(p, u) == find(p, v) else 0)
    print()
