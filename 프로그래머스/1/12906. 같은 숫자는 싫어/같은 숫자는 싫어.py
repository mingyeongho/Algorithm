def solution(arr):
    answer = [arr[0]]
    for n in range(1, len(arr)):
        if answer[-1] != arr[n]:
            answer.append(arr[n])
    return answer