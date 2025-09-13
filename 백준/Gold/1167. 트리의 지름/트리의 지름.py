import sys
from collections import defaultdict
input = sys.stdin.readline

V = int(input().strip())

tree = defaultdict(list)
for _ in range(V):
    node, *info, end = list(map(int, input().split()))
    for i in range(0, len(info), 2):
        n, c = info[i:i+2]
        tree[node].append((n, c))


def dfs(tree, cur) -> tuple[int, int]:
    stk = [cur]
    costs = [(-1, -1)] * (V+1)
    costs[cur] = (0, cur)  # (cost, index)
    while stk:
        xp = stk.pop()
        for nx in tree[xp]:
            n, c = nx
            if costs[n][0] > -1:
                continue
            costs[n] = (costs[xp][0] + c, n)
            stk.append(n)
    mx_cost, idx = max(costs)
    return (mx_cost, idx)


n1_cost, n1_index = dfs(tree, 1)
n2_cost, _ = dfs(tree, n1_index)
print(n2_cost)