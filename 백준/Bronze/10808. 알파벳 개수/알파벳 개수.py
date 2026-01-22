import sys
input = sys.stdin.readline

word = input().strip()
base = ord("a")

def func(word: str) -> list[int]:
    count = [0] * 26
    
    for alpha in word:
        count[ord(alpha) - base] += 1
    
    return count

print(*func(word))