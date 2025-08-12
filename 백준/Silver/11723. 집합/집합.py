import sys
input = sys.stdin.readline

M = int(input().strip())

S = set([])
for _ in range(M):
    cmd = input().split()

    if cmd[0] == "all":
        S.update([i for i in range(1, 21)])
    elif cmd[0] == "empty":
        S.clear()
    else:
        n = int(cmd[1])
        if cmd[0] == "add":
            S.add(n)
        elif cmd[0] == "remove":
            if n in S:
                S.remove(n)
        elif cmd[0] == "check":
            print(1 if n in S else 0)
        elif cmd[0] == "toggle":
            S.remove(n) if n in S else S.add(n)
