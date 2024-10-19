def solution(myString):
    answer = ''
    for i in range(len(myString) - 1, -1, -1):
        answer += myString[i]
    print(answer)
    return answer