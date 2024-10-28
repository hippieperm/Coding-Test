def solution(n, k):
    answer = []
    for i in range(1, n + 1):
        result = k * i
        if result <= n:
            answer.append(result)
    return answer