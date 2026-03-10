import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

N = int(input().strip())


# 원판 n개를 a번 장대에서 b번 장대로 옮기는 함수
def hanoi(a, b, n):
    if n == 1:
        print(f"{a} {b}")
        return
    hanoi(a, 6 - a - b, n - 1)
    print(f"{a} {b}")
    hanoi(6 - a - b, b, n - 1)


print((1 << N) - 1)
hanoi(1, 3, N)
