def solution(n):
    answer = 0
    for element in str(n):
        answer += int(element)
    return answer