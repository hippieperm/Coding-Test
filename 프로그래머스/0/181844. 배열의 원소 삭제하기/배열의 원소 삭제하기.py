def solution(arr, delete_list):
    answer = []
    for element in arr:
        if element not in delete_list:
            answer.append(element)
    return answer