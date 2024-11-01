def solution(s):
    pCnt = 0
    yCnt = 0

    for element in s.lower():
        if element == 'p':
            pCnt += 1
        elif element == 'y':
            yCnt += 1

    return pCnt == yCnt