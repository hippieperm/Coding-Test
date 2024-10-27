def solution(myString):
    answer = [myString[i:] for i in range(len(myString))]
    answer.sort()
    return answer