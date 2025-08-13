import sys

input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
  m = int(input().rstrip())

  zero = [0] * 41
  one = [0] * 41

  zero[0], zero[1] = 1, 0
  one[0], one[1] = 0, 1

  for i in range(2, m + 1):
    zero[i] = zero[i - 2] + zero[i - 1]
    one[i] = one[i - 2] + one[i - 1]
  print(zero[m], one[m])