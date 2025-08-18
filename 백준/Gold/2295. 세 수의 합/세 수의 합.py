import sys
input = sys.stdin.readline

N = int(input().strip())
A = [int(input().strip()) for _ in range(N)]
A.sort()

# 두 수 합 전처리 (i <= j로 자기 자신도 포함)
pair_sums = set()
for i in range(N):
    ai = A[i]
    for j in range(i, N):
        pair_sums.add(ai + A[j])

# 가장 큰 d부터 검사: d - c 가 두 수 합이면 d = a + b + c 성립
for l in range(N - 1, -1, -1):
    d = A[l]
    for k in range(N):
        if (d - A[k]) in pair_sums:
            print(d)
            sys.exit(0)
