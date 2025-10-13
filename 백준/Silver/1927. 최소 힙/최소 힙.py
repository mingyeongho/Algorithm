import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
hq = []
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        print(heapq.heappop(hq) if hq else 0)
    else:
        heapq.heappush(hq, x)
