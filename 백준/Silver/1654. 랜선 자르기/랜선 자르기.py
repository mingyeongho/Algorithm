import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [int(input().rstrip()) for _ in range(n)]


def solution(data: list, count: int) -> int:
  start = 1
  end = max(data)

  while start <= end:
    mid = (start + end) // 2
    sliced = [d // mid for d in data]
    if sum(sliced) >= count:
      start = mid + 1
    else:
      end = mid - 1

  return end


print(solution(data, m))