import sys
import math
input = sys.stdin.readline

N = int(input().strip())

# N < 2 인 경우 연속된 소수 합으로 N을 만들 수 없음
if N < 2:
    print(0)
    sys.exit(0)

# --- 에라토스테네스의 체 (2..N 소수) ---
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(math.isqrt(N)) + 1):
    if is_prime[i]:
        # i*i부터 i 간격으로 지우기
        for j in range(i * i, N + 1, i):
            is_prime[j] = False

primes = [i for i in range(2, N + 1) if is_prime[i]]

# --- 두 포인터(슬라이딩 윈도우)로 연속된 소수합이 N인 경우의 수 계산 ---
answer = 0
cur_sum = 0
start, end = 0, 0

while True:
    if cur_sum >= N:
        if cur_sum == N:
            answer += 1
        cur_sum -= primes[start]
        start += 1
    else:
        if end == len(primes):
            break
        cur_sum += primes[end]
        end += 1

print(answer)
