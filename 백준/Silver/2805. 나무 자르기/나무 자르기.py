import sys

input = sys.stdin.readline

n, m = map(int, input().split())
heights = list(map(int, input().split()))

start = 1
end = max(heights)


def binary(heights, m, start, end):
  if start > end:
    return end

  mid = (start + end) // 2
  total = sum([height - mid for height in heights if height >= mid])
  if total == m:
    return mid
  elif total > m:
    return binary(heights, m, mid + 1, end)
  else:
    return binary(heights, m, start, mid - 1)


print(binary(heights, m, start, end))
