def solution(myString):
    answer = []
    list = myString.split('x')
    for element in list:
        answer.append(len(element))
    return answer