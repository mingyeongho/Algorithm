import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
v1, v2 = map(int, input().split())


def dijkstra(graph, start, N):
    dist = [float("Inf")] * (N+1)
    dist[start] = 0
    hq = [(0, start)]

    while hq:
        cost, node = heapq.heappop(hq)

        if cost > dist[node]:
            continue

        for nxt_cost, nxt_node in graph[node]:
            new_cost = cost + nxt_cost
            if dist[nxt_node] > new_cost:
                dist[nxt_node] = new_cost
                heapq.heappush(hq, (new_cost, nxt_node))

    return dist


d = dijkstra(graph, 1, N)
dV1 = dijkstra(graph, v1, N)
dV2 = dijkstra(graph, v2, N)

route1 = d[v1] + dV1[v2] + dV2[N]
route2 = d[v2] + dV2[v1] + dV1[N]

answer = min(route1, route2)

print(answer if answer != float("Inf") else -1)
