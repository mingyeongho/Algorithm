import sys
input = sys.stdin.readline

N = int(input().strip())
seq = list(map(int, input().split()))

dp = [1] * N  # dp[i]는 seq[i]를 마지막 원소로 가지는 증가하는 부분 수열의 길이
for i in range(1, N):
    for j in range(i):
        if seq[i] > seq[j]:  # seq[i]가 seq[j]보다 크면 dp[i]는 dp[j]+1이다.
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
