def solution(arr, intervals):
    answer = []
    for element in intervals:
        for i in range(element[0], element[1] + 1):
            answer.append(arr[i])
    return answer