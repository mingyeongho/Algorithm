import sys

input = sys.stdin.readline

n = int(input().rstrip())
count = 0


def solution(s):
  global count
  stk = []
  for a in s:
    if not stk:
      stk.append(a)
    elif stk[-1] == a:
      stk.pop()
    else:
      stk.append(a)
  if not stk:
    count += 1


for _ in range(n):
  s = input().rstrip()

  solution(s)

print(count)
