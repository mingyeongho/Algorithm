import sys
from collections import deque

input = sys.stdin.readline

n, w, L = map(int, input().split())
T = deque(map(int, input().split()))
bridge = deque([0] * w)
current_weight = 0
time = 0
while bridge:
    time += 1

    current_weight -= bridge.popleft()

    if T:
        if current_weight + T[0] <= L:
            t = T.popleft()
            bridge.append(t)
            current_weight += t
        else:
            bridge.append(0)
    else:
        bridge.append(0)

    if current_weight == 0 and not T:
        break
print(time)
