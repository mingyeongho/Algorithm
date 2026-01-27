import sys

input = sys.stdin.readline

N = int(input().strip())
heights = [int(input().strip()) for _ in range(N)]


def solution(N, heights):
    answer = 0
    stk = []  # (키, 같은 키가 연속으로 등장하는 횟수)

    for i in range(N):  # 왼 -> 오 순회. 왼쪽 방향으로만 본다는 가정
        cnt = 1
        while stk and stk[-1][0] < heights[i]:
            answer += stk[-1][1]
            stk.pop()
        if stk and stk[-1][0] == heights[i]:  # 연속으로 같은 키의 사람이 등장했을 때
            answer += stk[-1][1]
            cnt += stk[-1][1]
            stk.pop()  # 같은 키인 사람이 연속으로 등장했기 때문에 이전 사람은 pop 해줘도 됨. 왜 와이? 뒤에 cnt 증가시킨 사람을 추가할거니까
        if stk:  # 옆에 있는 사람은 무조건 볼 수 있다.
            answer += 1
        stk.append((heights[i], cnt))

    return answer


print(solution(N, heights))