import sys
input = sys.stdin.readline

n = int(input().rstrip())
targets = set(map(int, input().split()))
m = int(input().rstrip())
datas = list(map(int, input().split()))

for data in datas:
    print(1 if data in targets else 0)