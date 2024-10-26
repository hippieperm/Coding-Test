def solution(numbers, n):
    answer = 0
    for element in numbers:
        answer += element
        if answer > n:
            break
    return answer