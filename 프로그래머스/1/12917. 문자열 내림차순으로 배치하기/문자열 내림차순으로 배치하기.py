def solution(s):
    answer = ''
    str_list = list(s)

    str_list.sort()
    for element in reversed(str_list):
        answer += element

    return answer