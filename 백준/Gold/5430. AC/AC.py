import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())


def solution(cmds, nums):
    direction = True
    for cmd in cmds:
        if cmd == 'R':
            direction = not direction
        else:
            if not nums or nums[0] == '':
                return None
            if direction:
                nums.popleft()
            else:
                nums.pop()
    if not direction:
        nums.reverse()
    return f"[{','.join(nums)}]"


for _ in range(n):
    cmds = input().strip()
    m = int(input().strip())
    nums = deque(input().strip()[1:-1].split(','))

    result = solution(cmds, nums)
    print(result if result else 'error')
