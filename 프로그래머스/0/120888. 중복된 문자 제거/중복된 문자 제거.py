def solution(myString):
    answer = ''
    for element in myString:
        if element not in answer:
            answer += element
    return answer