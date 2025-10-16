import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
mx_heap = []
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        if len(mx_heap) > 0:
            mx = heapq.heappop(mx_heap)
            print(-1 * mx)
        else:
            print(0)
    else:
        heapq.heappush(mx_heap, -1 * x)
