def solution(numbers):
    numbers.sort()
    length = len(numbers)
    return numbers[length - 2] * numbers[length - 1]