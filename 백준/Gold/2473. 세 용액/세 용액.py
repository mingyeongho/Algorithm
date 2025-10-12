import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
A.sort()

total = 3 * 10**9
ans = (0, 0, 0)

for i in range(N-2):
    left, right = i+1, N-1
    while left < right:
        s = A[i] + A[left] + A[right]
        if total > abs(s):
            total = abs(s)
            ans = (A[i], A[left], A[right])
            if s == 0:
                print(*ans)
                sys.exit(0)
        if s < 0:
            left += 1
        else:
            right -= 1
print(*ans)
