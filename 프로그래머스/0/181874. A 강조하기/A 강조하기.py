def solution(myString):
    answer = ''
    for element in myString:
        if element == 'a' or element == 'A':
            answer += element.upper()
        else:
            answer += element.lower()
    return answer