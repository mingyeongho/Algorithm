import sys

input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
  m = int(input().rstrip())
  clothes = {}
  result = 1
  for _ in range(m):
    name, case = input().split()
    if case in clothes:
      clothes[case].append(name)
    else:
      clothes[case] = [name]

  for key in clothes:
    result *= len(clothes[key]) + 1
  print(result - 1)
    