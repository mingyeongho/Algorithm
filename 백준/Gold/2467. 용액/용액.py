import sys
input = sys.stdin.readline

N = int(input().strip())
S = list(map(int, input().split()))

st = 0
en = N-1
answer = [float("Inf"), st, en]
while st < en:
    cur = S[st] + S[en]

    if abs(cur) < abs(answer[0]):
        answer = [cur, st, en]

    if cur == 0:
        print(S[st], S[en])
        exit(0)
    elif cur < 0:
        st = st + 1
    else:
        en = en - 1

print(S[answer[1]], S[answer[2]])
