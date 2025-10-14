import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

N, E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
v1, v2 = map(int, input().split())
INF = float("Inf")


def dijkstra(N, graph, x) -> list[int]:
    dist = [INF] * (N+1)
    dist[x] = 0
    hq = [(0, x)]
    while hq:
        cost, xp = heapq.heappop(hq)

        if cost > dist[xp]:
            continue

        for nxt_cost, nxt_node in graph[xp]:
            new_cost = cost + nxt_cost
            if dist[nxt_node] > new_cost:
                dist[nxt_node] = new_cost
                heapq.heappush(hq, (new_cost, nxt_node))
    return dist


dist = dijkstra(N, graph, 1)
dist1 = dijkstra(N, graph, v1)
dist2 = dijkstra(N, graph, v2)

path1 = dist[v1] + dist1[v2] + dist2[N]
path2 = dist[v2] + dist2[v1] + dist1[N]

answer = min(path1, path2)
print(answer if answer != INF else -1)
