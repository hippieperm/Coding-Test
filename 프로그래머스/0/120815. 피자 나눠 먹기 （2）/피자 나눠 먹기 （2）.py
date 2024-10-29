def solution(n):
    six = 0
    i = 1
    while True:
        six = n * i
        if six % 6 == 0:
            break
        i += 1
    return six // 6