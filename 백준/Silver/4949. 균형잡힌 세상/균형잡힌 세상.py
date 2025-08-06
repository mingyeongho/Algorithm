import sys
input = sys.stdin.readline


def solution(s):
    stk = []
    for w in s:
        if w == '(' or w == '[':
            stk.append(w)
        elif w == ')':
            if not stk:
                return False
            if stk[-1] != '(':
                return False
            stk.pop()
        elif w == ']':
            if not stk:
                return False
            if stk[-1] != '[':
                return False
            stk.pop()
    return False if stk else True


while True:
    s = input().rstrip()
    if s == '.':
        break
    print('yes' if solution(s) else 'no')
