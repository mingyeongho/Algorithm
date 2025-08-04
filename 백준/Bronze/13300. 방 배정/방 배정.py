import sys
import math

input = sys.stdin.readline

n, m = map(int, input().split())

male = [0] * 7
female = [0] * 7

for _ in range(n):
  sex, grade = map(int, input().split())
  if sex:
    male[grade] += 1
  else:
    female[grade] += 1


def solution(n, m, male, female):
  count = 0
  for i in range(1, 7):
    count += math.ceil(male[i] / m) + math.ceil(female[i] / m)
  return count


print(solution(n, m, male, female))