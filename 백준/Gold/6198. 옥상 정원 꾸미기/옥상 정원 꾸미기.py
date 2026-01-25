import sys
input = sys.stdin.readline

N = int(input().strip())
buildings = [int(input().strip()) for _ in range(N)]

def solution(N, buildings):
    answer = 0
    stk = [] # height

    for height in buildings:
        while stk and stk[-1] <= height:
            stk.pop()
        answer += len(stk)
        stk.append(height)

    return answer

print(solution(N, buildings))