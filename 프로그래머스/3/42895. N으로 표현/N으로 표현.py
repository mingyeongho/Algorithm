def solution(N, number):
    dp = [set() for _ in range(9)] # dp: N을 i번 사용해서 만들 수 있는 수들의 집합
    
    for i in range(1, 9):
        dp[i].add(int(str(N) * i)) # N, NN, NNN, ...
        
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(y - x)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
                    if x != 0:
                        dp[i].add(y // x)
        if number in dp[i]:
            return i
    return -1