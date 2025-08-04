import sys
input = sys.stdin.readline

A, B = [input().strip() for _ in range(2)]

alphabets = [[0, 0] for _ in range(26)]
for alpha in A:
    alphabets[ord(alpha) - 97][0] += 1
for alpha in B:
    alphabets[ord(alpha) - 97][1] += 1
answer = 0
for [l, r] in alphabets:
    answer += abs(l-r)
print(answer)
