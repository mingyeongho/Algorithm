import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    day = 0
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        count = 1
        speed = speeds.popleft()
        progress = progresses.popleft() + (day * speed)
        during = math.ceil((100 - progress) / speed)
        day += during
        while progresses and progresses[0] + (speeds[0] * day) >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        answer.append(count)
    return answer
