import sys

input = sys.stdin.readline

N = int(input().strip())
board = [list(map(int, input().split())) for _ in range(N)]

s_team = [None] * (N // 2)
visited = [False] * N
answer = float("Inf")


def get_ability(team: list[int]) -> int:
    ability = 0

    for i in team:
        for j in team:
            if i == j:
                continue
            ability += board[i][j]

    return ability


def backtrack(k, start):
    global answer

    if k == N // 2:
        # 팀 완성
        l_team = []
        for i in range(N):
            if not visited[i]:
                l_team.append(i)
        s_ability, l_ability = get_ability(s_team), get_ability(l_team)
        diff = abs(s_ability - l_ability)
        if diff == 0:
            print(0)
            exit(0)
        answer = min(answer, diff)
        return
    for i in range(start, N):
        if not visited[i]:
            s_team[k] = i
            visited[i] = True
            backtrack(k + 1, i + 1)
            visited[i] = False


backtrack(0, 0)
print(answer)
