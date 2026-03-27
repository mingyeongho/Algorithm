import sys

input = sys.stdin.readline

P = int(input().strip())
for _ in range(P):
    N, D, A, B, F = map(float, input().split())
    t = D / (A + B)
    answer = F * t

    print(int(N), f"{answer:.6f}")
