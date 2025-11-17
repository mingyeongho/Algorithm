import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(n)]

nums.sort()
print(*nums, sep='\n')
