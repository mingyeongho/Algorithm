import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input().strip())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))  # (cost, node)


def dijkstra(graph, start, N):
    dist = [float("Inf")] * (N+1)
    dist[start] = 0
    hq = [(0, start)]

    while hq:
        cost, node = heapq.heappop(hq)
        if dist[node] < cost:  # 이미 더 짧은 경로를 찾았으면 스킵
            continue
        for (nxt_cost, nxt_node) in graph[node]:
            new_cost = cost + nxt_cost
            if new_cost < dist[nxt_node]:
                dist[nxt_node] = new_cost
                heapq.heappush(hq, (new_cost, nxt_node))

    return dist


distance = dijkstra(graph, K, V)
for d in range(1, V+1):
    print(distance[d] if distance[d] != float("Inf") else "INF")
