def solution(numStr):
    answer = 0
    for element in numStr:
        answer += int(element)
    print(answer)
    return answer