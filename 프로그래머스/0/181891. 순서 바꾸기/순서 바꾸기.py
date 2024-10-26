def solution(numList, n):
    temp = numList[:n]
    answer = numList[n:] + temp
    return answer