import sys

input = sys.stdin.readline


def solution(ps):
    answer = 0
    temp = 0
    stk = []

    for brk in ps:
        if brk == "(":
            stk.append(brk)
        elif stk and stk[-1] == "(":
            stk.pop()
            answer += len(stk) + temp
            temp += len(stk)
            stk = []
        else:
            temp -= 1
            answer += 1
    return answer

ps = input().strip()
print(solution(ps))