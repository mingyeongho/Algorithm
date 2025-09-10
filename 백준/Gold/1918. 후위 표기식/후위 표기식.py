import sys
input = sys.stdin.readline

exp = input().strip()

answer = []
op = []
for n in exp:
    # 피연산자는 그대로 answer에 push
    if "A" <= n <= "Z":
        answer.append(n)
    # 연산자는 op 스택에 로직 수행
    else:
        # op의 top이 자신보다 우선순위가 낮으면 추가
        # op의 top이 자신과 우선순위가 같거나 높으면 자신보다 낮은게 나올 때까지 pop후 추가
        # +, -, *, /, (, )
        if n == "+" or n == "-":
            while op and op[-1] != "(":
                answer.append(op.pop())
            op.append(n)
        elif n == "*" or n == "/":
            while op and (op[-1] == "*" or op[-1] == "/"):
                answer.append(op.pop())
            op.append(n)
        elif n == "(":
            op.append(n)
        elif n == ")":
            while op and op[-1] != '(':
                answer.append(op.pop())
            op.pop()

while op:
    answer.append(op.pop())
print(*answer, sep='')
