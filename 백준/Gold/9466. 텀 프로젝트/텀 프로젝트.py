import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input().strip())


def dfs(x):
    global count
    visited[x] = True
    team.append(x)
    nxt = choice[x]
    if not visited[nxt]:
        dfs(nxt)
    else:
        if nxt in team:
            count += len(team[team.index(nxt):])


for _ in range(t):
    n = int(input().strip())
    choice = [0] + list(map(int, input().split()))

    visited = [True] + [False] * n
    count = 0
    for i in range(1, n+1):
        if not visited[i]:
            team = []
            dfs(i)

    print(n - count)
