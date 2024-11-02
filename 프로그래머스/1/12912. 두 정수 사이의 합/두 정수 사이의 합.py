def solution(a, b):
    answer = 0
    min_val = min(a, b)
    max_val = max(a, b)
    for i in range(min_val, max_val + 1):
        answer += i
    return answer