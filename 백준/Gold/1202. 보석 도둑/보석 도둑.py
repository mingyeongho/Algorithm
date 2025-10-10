import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = [tuple(map(int, input().split()))
          for _ in range(N)]  # (weight, value)
bags = [int(input()) for _ in range(K)]

# 1) 무게 오름차순으로 정렬
jewels.sort(key=lambda x: x[0])
# 2) 가방 수용 무게 오름차순 정렬
bags.sort()

ans = 0
j = 0  # jewels 포인터
max_heap = []  # 가격 최대 힙(음수로 넣어서 사용)

for cap in bags:
    # 3) 현재 가방(cap)에 들어갈 수 있는 모든 보석을 후보군에 추가
    while j < N and jewels[j][0] <= cap:
        w, v = jewels[j]
        heapq.heappush(max_heap, -v)  # 최대 힙처럼 쓰기 위해 음수 저장
        j += 1

    # 4) 후보군에서 가장 비싼 보석을 꺼내 담기
    if max_heap:
        ans += -heapq.heappop(max_heap)

print(ans)
