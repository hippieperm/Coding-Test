def solution(i, j, k):
    answer = 0
    for fi in range(i, j + 1):
        for element in str(fi):
            if element == str(k):
                answer += 1
    return answer