def solution(my_string, n):
    answer = ''
    for element in my_string:
        for i in range(n):
            answer += element
    return answer