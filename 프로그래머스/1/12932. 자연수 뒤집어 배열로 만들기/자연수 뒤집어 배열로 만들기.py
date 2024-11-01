def solution(n):
    answer = []
    for element in str(n):
        answer.append(int(element))
    return answer[::-1]