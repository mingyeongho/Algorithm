import sys
input = sys.stdin.readline

S = input().split("-")
answer = []
for s in S:
    a = map(int, s.split("+"))
    answer.append(sum(a))
ans = answer[0]
for i in range(1, len(answer)):
    ans -= answer[i]
print(ans)
