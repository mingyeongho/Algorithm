import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 집과 치킨집 좌표 저장
houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            chickens.append((i, j))

# 치킨집 선택
selected = [-1] * M
answer = float("Inf")


def backtrack(start, k):
    global answer

    if k == M:
        # 치킨집 선택 완료
        total = 0
        for hx, hy in houses:
            dist = float("Inf")
            for idx in selected:
                cx, cy = chickens[idx]
                dist = min(dist, abs(hx-cx) + abs(hy-cy))
            total += dist
        answer = min(answer, total)
        return
    for i in range(start, len(chickens)):
        selected[k] = i
        backtrack(i+1, k+1)


backtrack(0, 0)

print(answer)
