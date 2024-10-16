def solution(my_string):
    answer = ''
    for char in my_string:
        if char.islower():
            answer += char.upper()
        elif char.isupper():
            answer += char.lower()
    return answer