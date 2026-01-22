import sys
input = sys.stdin.readline

A = int(input().strip())
B = int(input().strip())
C = int(input().strip())

def func(arr: list[int]) -> list[int]:
    temp = str(A * B * C)
    count = [0] * 10
    
    for t in temp:
        count[int(t)] += 1
    
    return count

print(*func([A, B, C]), sep='\n')