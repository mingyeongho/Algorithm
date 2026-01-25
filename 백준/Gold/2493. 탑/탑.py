import sys
input = sys.stdin.readline

N = int(input().strip())
towers = list(map(int, input().split()))

def solution(N, towers):
    answer = [0] * N
    stk = [] # (인덱스, 높이)
    
    for i, tower in enumerate(towers):
        while stk and stk[-1][1] < tower:
            stk.pop()
        if stk and stk[-1][1] > tower:
            answer[i] = stk[-1][0] + 1
        stk.append((i, tower))
        
    return " ".join(map(str, answer))

print(solution(N, towers))