import sys
input = sys.stdin.readline

N, M = map(int, input().split())

visited = [False] * (N+1)
answer = [0] * M


def backtrack(k):
    if k == M:
        print(*answer)
        return
    for i in range(1, N+1):
        if not visited[i]:
            answer[k] = i
            visited[i] = True
            backtrack(k+1)
            visited[i] = False


backtrack(0)
