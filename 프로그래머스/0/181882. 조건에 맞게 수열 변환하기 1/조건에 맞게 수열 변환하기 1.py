def solution(arr):
    answer = []
    for element in arr:
        result = (element >= 50 and element % 2 == 0) \
            and (element // 2) \
            or (element <= 50 and element % 2 == 1 and element * 2) \
            or element
        answer.append(result)
    return answer