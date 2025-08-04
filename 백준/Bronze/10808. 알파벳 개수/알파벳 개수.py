import sys

input = sys.stdin.readline

s = input().rstrip()

alpha = [0] * 26
for w in s:
    alpha[ord(w) - ord('a')] += 1

print(*alpha)
