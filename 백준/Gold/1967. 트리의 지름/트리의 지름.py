import sys
import heapq
input = sys.stdin.readline

INF = float("Inf")


def dijkstra(graph, N, x):
    dist = [INF] * (N+1)
    dist[x] = 0
    hq = [(0, x)]
    while hq:
        cost, node = heapq.heappop(hq)
        if cost > dist[node]:
            continue
        for nxt_cost, nxt_node in graph[node]:
            new_cost = dist[node] + nxt_cost
            if dist[nxt_node] > new_cost:
                dist[nxt_node] = new_cost
                heapq.heappush(hq, (new_cost, nxt_node))
    idx = dist.index(max(dist[1:]))
    return dist[1:], idx


N = int(input().strip())
graph = [[] * (N+1) for _ in range(N+1)]
for _ in range(N-1):
    u, v, c = map(int, input().split())
    graph[u].append((c, v))
    graph[v].append((c, u))

dist, idx = dijkstra(graph, N, 1)
dist2, idx2 = dijkstra(graph, N, idx)
print(max(dist2))
