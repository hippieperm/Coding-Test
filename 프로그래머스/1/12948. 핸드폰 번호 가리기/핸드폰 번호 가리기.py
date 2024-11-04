def solution(phoneNumber):
    answer = ''
    for i in range(len(phoneNumber)):
        if i < len(phoneNumber) - 4:
            answer += '*'
        else:
            answer += phoneNumber[i]
    return answer