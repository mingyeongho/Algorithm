import sys

input = sys.stdin.readline

n, m = map(int, input().split())

s = set()
res = []
for _ in range(n):
  name = input().rstrip()
  s.add(name)

for _ in range(m):
  name = input().rstrip()
  if name in s:
    res.append(name)

print(len(res))
print(*sorted(res), sep='\n')