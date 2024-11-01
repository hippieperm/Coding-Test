def solution(arr):
    answer = 0
    for element in arr:
        answer += element
    return answer / len(arr) if arr else 0