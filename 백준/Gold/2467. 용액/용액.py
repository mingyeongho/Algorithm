import sys
input = sys.stdin.readline

N = int(input().strip())
S = list(map(int, input().split()))

l, r = 0, N - 1
best_abs = float('inf')
ans_l, ans_r = S[l], S[r]

while l < r:
    s = S[l] + S[r]
    a = abs(s)

    if a < best_abs:
        best_abs = a
        ans_l, ans_r = S[l], S[r]
        if best_abs == 0:
            break

    # 합이 0보다 작으면 값(합)을 키워야 하므로 l를 오른쪽으로 이동
    if s < 0:
        l += 1
    else:
        r -= 1

print(ans_l, ans_r)
