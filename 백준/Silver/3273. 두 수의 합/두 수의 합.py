import sys

input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().split()))
x = int(input().rstrip())


def fn(n, arr, x):
  nums = [0] * 1_000_001
  cnt = 0
  for a in arr:
    if x >= a and 1 <= x-a <= 1_000_000 and nums[x - a]:
      cnt += 1
    nums[a] = 1
  return cnt


print(fn(n, arr, x))