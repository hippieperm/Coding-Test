def solution(my_string):
    answer = ''
    check = 'aeiou'
    for element in my_string:
        if element not in check:
            answer += element
    return answer