def solution(dot):
    indexX = dot[0]
    indexY = dot[1]

    if indexX > 0 and indexY > 0:
        return 1
    elif indexX < 0 and indexY > 0:
        return 2
    elif indexX < 0 and indexY < 0:
        return 3
    elif indexX > 0 and indexY < 0:
        return 4
    return 0