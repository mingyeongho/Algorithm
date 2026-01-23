import sys

input = sys.stdin.readline

n = int(input().rstrip())


def solution(logger):
  head, tail = [], []
  for log in logger:
    if log == '<':
      if head:
        tail.append(head.pop())
    elif log == '>':
      if tail:
        head.append(tail.pop())
    elif log == '-':
      if head:
        head.pop()
    else:
      head.append(log)
  tail.reverse()
  head.extend(tail)
  return "".join(head)


for _ in range(n):
  logger = input().rstrip()
  result = solution(logger)
  print(result)
