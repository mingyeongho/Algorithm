import sys

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))  # 수열
OP = list(map(int, input().split()))  # 연산자 개수

mn, mx = float("Inf"), float("-Inf")
value = A[0]
cur = 1


def backtrack(k):
    global value, cur, mn, mx

    if k == N - 1:
        mx = max(mx, value)
        mn = min(mn, value)
        return
    for i in range(len(OP)):
        if OP[i] > 0:
            OP[i] -= 1
            prev = value
            if i == 0:
                value += A[cur]
            elif i == 1:
                value -= A[cur]
            elif i == 2:
                value *= A[cur]
            elif i == 3:
                if value < 0:
                    value = -((-value) // A[cur])
                else:
                    value //= A[cur]

            cur += 1
            backtrack(k + 1)
            cur -= 1
            value = prev
            OP[i] += 1


backtrack(0)

print(mx)
print(mn)
