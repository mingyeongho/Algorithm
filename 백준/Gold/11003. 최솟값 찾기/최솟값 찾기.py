import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))


def solution(N, A, L):
    deq = deque([])  # (idx, A[idx])
    answer = []

    for i in range(N):
        while deq and deq[-1][1] > A[i]:
            deq.pop()
        deq.append((i, A[i]))

        if deq[0][0] < i - L + 1:
            deq.popleft()

        answer.append(deq[0][1])

    return answer


print(*solution(N, A, L))