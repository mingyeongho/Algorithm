def solution(s):
    stk = []
    
    for b in s:
        if b == "(":
            stk.append(b)
        else:
            if not stk:
                return False
            if stk[-1] != "(":
                return False
            stk.pop()
    if stk:
        return False
    return True