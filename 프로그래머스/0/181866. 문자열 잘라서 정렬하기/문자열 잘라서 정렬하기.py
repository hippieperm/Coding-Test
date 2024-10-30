def solution(myString):
    answer = []
    str_list = myString.split('x')
    for element in str_list:
        if element != '':
            answer.append(element)
    answer.sort()
    return answer