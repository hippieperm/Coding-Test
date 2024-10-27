def solution(my_string, indexList):
    answer = ''
    for element in indexList:
        answer += my_string[element]
    return answer