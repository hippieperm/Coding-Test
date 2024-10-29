def solution(age):
    answer = ''
    list_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for element in str(age):
        answer += list_str[int(element)]
    return answer