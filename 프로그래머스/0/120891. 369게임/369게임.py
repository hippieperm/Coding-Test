def solution(order):
    answer = 0
    for element in str(order):
        answer += 1 if element in ['3', '6', '9'] else 0
    return answer