import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
tree = defaultdict(list)
for _ in range(m):
    s, e, c = map(int, input().split())
    tree[s].append((c, e))
S, E = map(int, input().split())


def dijkstra(start):
    dist = [1e9] * (n+1)
    dist[start] = 0
    hq = [(0, start)]
    path = [-1] * (n+1)

    while hq:
        cost, node = heapq.heappop(hq)
        if cost > dist[node]:
            continue

        for nxt_cost, nxt_node in tree[node]:
            new_cost = cost + nxt_cost
            if dist[nxt_node] > new_cost:
                dist[nxt_node] = new_cost
                heapq.heappush(hq, (new_cost, nxt_node))
                path[nxt_node] = node
    return dist, path


d, p = dijkstra(S)
print(d[E])
path = [E]
while p[E] != S:
    path.append(p[E])
    E = p[E]
path.append(S)
path.reverse()
print(len(path))
print(*path)