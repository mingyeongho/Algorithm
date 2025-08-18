import sys

input = sys.stdin.readline

n = int(input().rstrip())
targets = map(int, input().split())
m = int(input().rstrip())
datas = list(map(int, input().split()))

targetDict = dict()

for target in targets:
  if targetDict.get(target):
    targetDict[target] += 1
  else:
    targetDict[target] = 1

for data in datas:
  print(0 if not targetDict.get(data) else targetDict.get(data), end=' ')