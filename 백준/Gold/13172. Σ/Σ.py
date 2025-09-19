import sys
import math
input = sys.stdin.readline

MOD = 1_000_000_007

M = int(input().strip())


def dc(N, x):
    if x == 1:
        return N
    half = dc(N, x//2)
    if x % 2 == 0:
        return half * half % MOD
    else:
        return half * half * N % MOD


total = 0
for _ in range(M):
    N, S = map(int, input().split())
    gcd = math.gcd(N, S)
    N //= gcd
    S //= gcd

    total += S * dc(N, MOD-2) % MOD
    total %= MOD

print(total)
