import sys

input = sys.stdin.readline

N = int(input().strip())


def func(a, b, n):
    if n == 1:
        print(f"{a} {b}")
        return
    func(a, 6 - a - b, n - 1)
    print(f"{a} {b}")
    func(6 - a - b, b, n - 1)


print((1 << N) - 1)
func(1, 3, N)
