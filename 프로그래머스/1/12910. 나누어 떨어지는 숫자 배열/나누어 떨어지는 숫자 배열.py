def solution(arr, divisor):
    answer = []
    arr.sort()
    for element in arr:
        if element % divisor == 0:
            answer.append(element)
    if not answer:
        answer.append(-1)
    return answer