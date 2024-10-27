def solution(myString, num1, num2):
    answer = ''
    for i in range(len(myString)):
        if i == num1:
            answer += myString[num2]
        elif i == num2:
            answer += myString[num1]
        else:
            answer += myString[i]
    return answer