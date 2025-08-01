""" 
시간제한: 0.5초, 1 <= N <= 1_000, 1 <= M <= 100_000.

출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 구하는 문제.
출발 도시가 정해져 있으므로 다익스트라 알고리즘을 사용하여 문제를 해결할 수 있다.
"""
import sys
input = sys.stdin.readline

N = int(input().strip())  # 도시의 개수
M = int(input().strip())  # 버스의 개수

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

s, e = map(int, input().split())

dist = [float("inf")] * (N+1)
visited = [False] * (N+1)


def get_mn_idx():  # 방문하지 않은 노드들 중 가장 비용이 작은 노드 번호를 반환
    mn_value = float("inf")
    idx = 0
    for i in range(1, N+1):
        if dist[i] < mn_value and not visited[i]:
            mn_value = dist[i]
            idx = i
    return idx


def dijkstra(start):
    dist[start] = 0
    visited[start] = True

    for (end, cost) in graph[start]:
        if dist[end] > cost:
            dist[end] = cost

    for _ in range(N-1):
        mn_idx = get_mn_idx()
        visited[mn_idx] = True
        for (nxt_end, nxt_cost) in graph[mn_idx]:
            c = dist[mn_idx] + nxt_cost
            if c < dist[nxt_end]:
                dist[nxt_end] = c


dijkstra(s)

print(dist[e])
