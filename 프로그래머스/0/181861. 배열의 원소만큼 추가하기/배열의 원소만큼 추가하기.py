def solution(arr):
    answer = []
    for element in arr:
        for i in range(element):
            answer.append(element)
    return answer