import sys

input = sys.stdin.readline

n = int(input().rstrip())


# 사용한 알파벳의 개수가 같은가
def isStrfry(original, result):
  origin_alpha = [0] * 26
  result_alpha = [0] * 26
  for alpha in original:
    origin_alpha[ord(alpha) - 97] += 1
  for alpha in result:
    result_alpha[ord(alpha) - 97] += 1
  for i in range(26):
    if origin_alpha[i] != result_alpha[i]:
      return False
  return True


for _ in range(n):
  original, result = input().split()
  print("Possible" if isStrfry(original, result) else "Impossible")