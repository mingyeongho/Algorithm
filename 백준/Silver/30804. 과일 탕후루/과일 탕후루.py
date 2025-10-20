import sys
input = sys.stdin.readline

N = int(input().strip())
seq = list(map(int, input().split()))

en = 0
fruits = [0] * 10
fruits[seq[0]] = 1
kind = 1
answer = 1

for st in range(N):
    while en + 1 < N and kind <= 2:
        if fruits[seq[en + 1]] == 0 and kind == 2:
            break
        en += 1
        if fruits[seq[en]] == 0:
            kind += 1
        fruits[seq[en]] += 1

    answer = max(answer, en - st + 1)

    fruits[seq[st]] -= 1
    if fruits[seq[st]] == 0:
        kind -= 1

print(answer)
