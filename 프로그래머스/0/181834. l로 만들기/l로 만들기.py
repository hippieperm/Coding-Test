def solution(my_string):
    answer = ''
    val = 'abcdefghijk'
    for element in my_string:
        if element in val:
            answer += 'l'
        else:
            answer += element
    return answer