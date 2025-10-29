import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
A.sort()

answer = 0

for i in range(N):
    temp = A[:i] + A[i+1:]
    st, en = 0, len(temp) - 1

    while st < en:
        s = temp[st] + temp[en]

        if s == A[i]:
            answer += 1
            break
        elif s < A[i]:
            st += 1
        else:
            en -= 1

print(answer)
