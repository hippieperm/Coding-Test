def solution(myString, target):
    result = 0
    for i in range(len(myString) - len(target) + 1):
        if myString[i:i + len(target)] == target:
            result = 1
    return result