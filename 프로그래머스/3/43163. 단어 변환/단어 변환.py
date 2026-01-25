from collections import deque

# begin과 target이 한 글자만 다른지 판별
def isDistinction(begin, target):
    diff = 0
    for i in range(len(begin)):
        if begin[i] != target[i]:
            diff += 1
        if diff > 1:
            return False
    return True if diff == 1 else False

def solution(begin, target, words):
    if target not in words:
        return 0
    
    N = len(words)
    dist = [-1] * N
    
    deq = deque([(0, begin)]) # dist, word
    while deq:
        prev_dist, prev_word = deq.popleft()
        for i, w in enumerate(words):
            if dist[i] == -1 and isDistinction(prev_word, w):
                dist[i] = prev_dist + 1
                deq.append((dist[i], w))
    return dist[words.index(target)]