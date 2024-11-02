def solution(seoul):
    for i in range(len(seoul)):
        if 'Kim' in seoul[i]:
            return f"김서방은 {i}에 있다"
    return ''