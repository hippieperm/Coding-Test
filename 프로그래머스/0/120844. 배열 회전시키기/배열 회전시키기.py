def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer.append(numbers.pop())
        answer.extend(numbers)
    else:
        i = numbers.pop(0)
        answer.extend(numbers)
        answer.append(i)
    return answer