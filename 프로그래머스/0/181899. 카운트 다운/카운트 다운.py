def solution(startNum, endNum):
    answer = []
    for i in range(startNum, endNum - 1, -1):
        answer.append(i)
    return answer