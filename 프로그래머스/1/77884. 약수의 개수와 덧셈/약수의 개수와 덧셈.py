def solution(left, right):
    answer = 0
    oddEven = 0

    for i in range(left, right + 1):
        oddEven = 0
        for k in range(1, (i // 2) + 1):
            if i % k == 0:
                oddEven += 1
        if oddEven % 2 == 0:
            answer += i
        else:
            answer -= i

    return answer * -1