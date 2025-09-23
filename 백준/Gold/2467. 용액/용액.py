import sys
input = sys.stdin.readline

N = int(input().strip())
S = list(map(int, input().split()))

left, right = 0, N-1
mn = 2_000_000_001
ans_left, ans_right = S[left], S[right]

while left < right:
    s = S[left] + S[right]
    a = abs(s)

    if a < mn:
        mn = a
        ans_left, ans_right = S[left], S[right]
        if mn == 0:
            break
    if s < 0:
        left += 1
    else:
        right -= 1

print(ans_left, ans_right)
