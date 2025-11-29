import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

arr = deque([i for i in range(1, n+1)])
count = 0
for num in nums:
    idx = arr.index(num)

    # num을 맨 앞으로 가져오는 로직
    if idx > len(arr) // 2:
        arr.rotate(len(arr) - idx)
        count += len(arr) - idx
    else:
        arr.rotate(-(idx))
        count += idx

    arr.popleft()

print(count)
