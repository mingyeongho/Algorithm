import sys

input = sys.stdin.readline

n = input().rstrip()


def fn(n):
  cnts = [0] * 10
  for i in n:
    if i == '6' or i == '9':
      if cnts[6] <= cnts[9]:
        cnts[6] += 1
      else:
        cnts[9] += 1
    else:
      cnts[int(i)] += 1
  return max(cnts)


print(fn(n))