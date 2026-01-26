import sys
input = sys.stdin.readline

N = int(input().strip())
array = list(map(int, input().split()))

def solution(N, array):
    answer = [-1] * N
    stk = [] # n
    
    for i in range(N-1, -1, -1):
        current = array[i]
        while stk and stk[-1] <= current:
            stk.pop()
        if stk:
            answer[i] = stk[-1]
        stk.append(current)
    return " ".join(map(str, answer))

print(solution(N, array))