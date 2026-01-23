# use stack

import sys

input = sys.stdin.readline

head = list(input().rstrip())
tail = []

n = int(input().rstrip())
for _ in range(n):
  cmd = input().split()

  if cmd[0] == 'L':
    if head:
      tail.append(head.pop())
  elif cmd[0] == 'D':
    if tail:
      head.append(tail.pop())
  elif cmd[0] == 'B':
    if head:
      head.pop()
  else:
    head.append(cmd[1])

tail.reverse()
head.extend(tail)
print(''.join(head))
