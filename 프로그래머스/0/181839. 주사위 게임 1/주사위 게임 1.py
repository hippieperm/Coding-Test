def solution(a, b):
    if a % 2 != 0 and b % 2 != 0:
        answer = (a * a) + (b * b)
    elif a % 2 != 0 or b % 2 != 0:
        answer = 2 * (a + b)
    else:
        answer = a - b

    if answer < 0:
        answer *= -1

    return answer