def solution(prices):
    n = len(prices)
    answer = [0] * n
    stk = []
    
    for i, price in enumerate(prices):
        while stk and stk[-1][1] > price:
            idx, prev_price = stk.pop()
            answer[idx] = i - idx
        stk.append((i, price))

    while stk:
        idx, price = stk.pop()
        answer[idx] = (n - 1) - idx
    
    return answer