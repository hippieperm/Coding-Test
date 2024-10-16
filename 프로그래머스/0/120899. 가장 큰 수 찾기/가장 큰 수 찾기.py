def solution(array):
    answer = []
    max_val = 0
    for i in range(len(array) - 1):
        max_val = array[i]
        answer = [array[i], i]
        if max_val < array[i + 1]:
            answer = [array[i + 1], i + 1]
    print(answer)
    return answer