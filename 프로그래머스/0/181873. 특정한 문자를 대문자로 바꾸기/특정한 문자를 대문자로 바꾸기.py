def solution(myString, alp):
    answer = ''
    for element in myString:
        answer += element.upper() if element == alp else element
    return answer