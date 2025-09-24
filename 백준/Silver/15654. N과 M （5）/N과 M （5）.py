import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(map(int, input().split()))
S.sort()

visited = [False] * N
answer = []


def backtrack(k):
    if k == M:
        print(*answer)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            answer.append(S[i])
            backtrack(k+1)
            visited[i] = False
            answer.pop()


backtrack(0)
