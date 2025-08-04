import sys
input = sys.stdin.readline

a, b, c = [int(input().rstrip()) for _ in range(3)]
count = [0] * 10

for r in str(a * b * c):
    count[int(r)] += 1

print(*count, sep='\n')
