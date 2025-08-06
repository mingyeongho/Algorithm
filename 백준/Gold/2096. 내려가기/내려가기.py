import sys
input = sys.stdin.readline

N = int(input().strip())

init = list(map(int, input().split()))
mn_dp = init
mx_dp = init

for _ in range(N-1):
    a, b, c = map(int, input().split())
    mn_dp = [a + min(mn_dp[0], mn_dp[1]), b + min(mn_dp),
             c + min(mn_dp[1], mn_dp[2])]
    mx_dp = [a + max(mx_dp[0], mx_dp[1]), b + max(mx_dp),
             c + max(mx_dp[1], mx_dp[2])]
print(max(mx_dp), min(mn_dp))
