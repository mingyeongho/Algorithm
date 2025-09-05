import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input().strip())
tree = defaultdict(list)
for _ in range(N-1):
    parent, child, cost = map(int, input().split())
    tree[parent].append((child, cost))
    tree[child].append((parent, cost))


def dfs(cur: int) -> tuple[int, int]:
    stk = [cur]
    costs = [(-1, -1)] * (N+1)
    costs[cur] = (0, cur)
    while stk:
        xp = stk.pop()
        for nx, cost in tree[xp]:
            if costs[nx][0] > -1:
                continue
            costs[nx] = (costs[xp][0] + cost, nx)
            stk.append(nx)
    mx, idx = max(costs)

    return (idx, mx)


n1, n1_cost = dfs(1)
n2, n2_cost = dfs(n1)
print(n2_cost)
