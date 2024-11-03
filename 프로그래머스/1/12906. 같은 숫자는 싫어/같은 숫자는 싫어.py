def solution(arr):
    answer = []
    for i in range(len(arr)):
        if not answer or answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer