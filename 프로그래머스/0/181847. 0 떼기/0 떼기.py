def solution(nStr):
    cnt = 0
    for element in nStr:
        if element == '0':
            cnt += 1
        else:
            break
    return nStr[cnt:]