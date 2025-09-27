import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = [0] * M
res = set()
is_used = [False] * (N+1)


def backtrack(k):
    if k == M:
        result = ' '.join(map(str, ans))
        res.add(result)
        return
    for i in range(N):
        if not is_used[i]:
            ans[k] = nums[i]
            is_used[i] = True
            backtrack(k+1)
            is_used[i] = False


backtrack(0)

res = sorted(res, key=lambda x: list(map(int, x.split())))
for r in res:
    print(r)
