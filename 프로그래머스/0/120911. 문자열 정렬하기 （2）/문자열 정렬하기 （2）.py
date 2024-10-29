def solution(my_string):
    answer = my_string.lower()
    result = ''.join(sorted(answer))
    return result