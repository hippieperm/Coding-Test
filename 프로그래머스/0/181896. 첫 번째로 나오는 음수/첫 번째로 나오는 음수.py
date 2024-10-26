def solution(numList):
    answer = -1
    for i in range(len(numList)):
        if numList[i] < 0:
            answer = i
            break
    return answer