def solution(strArr):
    answer = []
    for element in strArr:
        if 'ad' not in element:
            answer.append(element)
    return answer