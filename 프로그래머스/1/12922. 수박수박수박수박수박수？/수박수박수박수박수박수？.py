def solution(n):
    answer = ''
    su = '수'
    park = '박'

    for i in range(n):
        if i % 2 == 0:
            answer += su
        else:
            answer += park
    return answer