def solution(myString):
    answer = [int(element) for element in myString if element.isdigit()]
    answer.sort()
    return answer