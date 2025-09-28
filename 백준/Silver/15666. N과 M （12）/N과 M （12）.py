import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = [0] * M
res = set()


def backtrack(k, start):
    if k == M:
        result = ' '.join(map(str, ans))
        res.add(result)
        return
    for i in range(start, N):
        ans[k] = nums[i]
        backtrack(k+1, i)


backtrack(0, 0)

res = sorted(res, key=lambda x: list(map(int, x.split())))
for r in res:
    print(r)
