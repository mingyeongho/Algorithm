import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
a = A.intersection(B)
print(N - len(a))
print(*sorted(A.difference(B)))
