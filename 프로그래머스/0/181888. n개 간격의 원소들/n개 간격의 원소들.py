def solution(numList, n):
    answer = []

    for i in range(len(numList)):
        if i % n == 0:
            answer.append(numList[i])
    return answer