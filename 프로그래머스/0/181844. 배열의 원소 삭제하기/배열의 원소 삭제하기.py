def solution(arr, delete_list):
    result = []
    for element in arr:
        if element not in delete_list:
            result.append(element)
    return result