def solution(str_list, ex):
    answer = ''
    for element in str_list:
        if ex not in element:
            answer += element
    print(answer)
    return answer