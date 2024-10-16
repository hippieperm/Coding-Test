def solution(n, t):
    answer = 0
    for i in range(t):
        if answer != 0:
            answer = answer * 2
        else:
            answer = n * 2
    print(answer)
    return answer