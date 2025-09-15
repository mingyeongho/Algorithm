import sys
input = sys.stdin.readline


def bf(N, edges):
    dist = [1e9] * (N+1)
    dist[1] = 0

    for i in range(N):
        for cur, nxt, cost in edges:  # 매 반복마다 모든 간선을 확인
            if dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost
                if i == N-1:
                    return True
    return False


TC = int(input().strip())

for _ in range(TC):
    N, M, W = map(int, input().split())
    edges = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    print("YES" if bf(N, edges) else "NO")
