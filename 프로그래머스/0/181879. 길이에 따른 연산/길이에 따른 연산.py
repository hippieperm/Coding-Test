def solution(numList):
    answer = 1
    if len(numList) >= 11:
        answer = 0
        for element in numList:
            answer += element
    else:
        for element in numList:
            answer *= element
    return answer