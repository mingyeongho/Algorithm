import sys

input = sys.stdin.readline

n = int(input().rstrip())
points = list(map(int, input().split()))

sorted_points = sorted(set(points))
dict = dict(zip(sorted_points, range(len(sorted_points))))
print(*[dict[point] for point in points])
