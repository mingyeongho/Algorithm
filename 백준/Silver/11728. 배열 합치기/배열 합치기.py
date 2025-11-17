import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []
a_idx, b_idx = 0, 0
while True:
    if a_idx > N-1:
        ans += B[b_idx:]
        break
    elif b_idx > M-1:
        ans += A[a_idx:]
        break

    if A[a_idx] > B[b_idx]:
        ans.append(B[b_idx])
        b_idx += 1
    else:
        ans.append(A[a_idx])
        a_idx += 1

print(*ans)
