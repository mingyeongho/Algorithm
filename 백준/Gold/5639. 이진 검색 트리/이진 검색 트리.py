import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def post(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start+1, end+1):
        if pre[start] < pre[i]:
            mid = i
            break
    post(start+1, mid-1)
    post(mid, end)
    print(pre[start])


pre = []
while True:
    try:
        n = int(input().strip())
        pre.append(n)
    except:
        break

post(0, len(pre)-1)
