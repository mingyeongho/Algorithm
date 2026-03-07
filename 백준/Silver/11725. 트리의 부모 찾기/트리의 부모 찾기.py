import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

N = int(input().strip())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0, 1] + [-1] * (N - 1)


def dfs(start, tree, parents):
    for nx in tree[start]:
        if parents[nx] == -1:
            parents[nx] = start
            dfs(nx, tree, parents)


dfs(1, tree, parents)

print(*parents[2:], sep="\n")
