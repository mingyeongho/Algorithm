import sys
import math

input = sys.stdin.readline

n = int(input().rstrip())


def solution(n):
  # √n이 정수일 때
  if math.isqrt(n)**2 == n:
    return 1

  # √(n - i^2)이 정수일 때
  for i in range(1, math.isqrt(n) + 1):
    if math.isqrt(n - i**2) == math.sqrt(n - i**2):
      return 2

  # √(n - i^2 - j^2)이 정수일 때
  for i in range(1, math.isqrt(n) + 1):
    for j in range(1, math.isqrt(n - i**2) + 1):
      if math.isqrt(n - i**2 - j**2) == math.sqrt(n - i**2 - j**2):
        return 3

  return 4


print(solution(n))