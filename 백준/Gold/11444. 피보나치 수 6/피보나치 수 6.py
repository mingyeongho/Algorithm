import sys
input = sys.stdin.readline

MOD = 1_000_000_007

n = int(input().strip())


def fibo(n):
    if n == 0:
        return (0, 1)
    a, b = fibo(n >> 1)  # n을 반으로 쪼개기, a = F_k, b = F_k+1
    t = (2 * b - a) % MOD
    c = (a * t) % MOD  # F_2k
    d = (a*a + b*b) % MOD  # F_2k+1
    if n & 1:
        return (d, (c + d) % MOD)
    return (c, d)


print(fibo(n)[0])
