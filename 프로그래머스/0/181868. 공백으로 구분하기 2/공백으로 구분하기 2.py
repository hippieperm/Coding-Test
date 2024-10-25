def solution(myString):
    answer = []
    for element in myString.split(' '):
        if element != ' ' and element != '':
            answer.append(element)
    return answer