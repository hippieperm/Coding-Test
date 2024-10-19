def solution(numList, n):
    answer = 0
    for element in numList:
        if element == n:
            answer = 1
            break
        answer = 0
    return answer