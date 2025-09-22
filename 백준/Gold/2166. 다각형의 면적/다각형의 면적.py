import sys
input = sys.stdin.readline

n = int(input().strip())
points = [list(map(int, input().split())) for _ in range(n)]

area = 0
for i in range(n):
    j = (i + 1) % n
    area += points[i][0] * points[j][1] - points[j][0] * points[i][1]
print(abs(area / 2.0))
