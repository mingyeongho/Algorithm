import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
M = int(input().strip())
B = list(map(int, input().split()))


def recur(A: list[int], B: list[int], res: list[int]):
    if not A or not B:
        return res

    mx_a, mx_b = max(A), max(B)
    idx_a, idx_b = A.index(mx_a), B.index(mx_b)

    if mx_a == mx_b:
        res.append(mx_a)
        return recur(A[idx_a+1:], B[idx_b+1:], res)
    elif mx_a > mx_b:
        A.pop(idx_a)
        return recur(A, B, res)
    else:
        B.pop(idx_b)
        return recur(A, B, res)


res = recur(A, B, [])
print(len(res))
print(*res)
