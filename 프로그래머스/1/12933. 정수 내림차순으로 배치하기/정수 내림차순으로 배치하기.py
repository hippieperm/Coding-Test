def solution(n):
    int_answer = 0
    str_answer = ''
    lst = []

    for element in str(n):
        lst.append(int(element))

    lst.sort()

    for element in reversed(lst):
        str_answer += str(element)

    int_answer = int(str_answer)
    return int_answer