def solution(my_string):
    answer = 0
    for char in my_string:
        num = int(char) if char.isdigit() else None
        if num is not None:
            answer += num
    return answer