def solution(arr):
    if len(arr) <= 1:  # 배열의 길이가 1 이하인 경우
        return [-1]  # -1을 포함하는 배열 반환

    original_list = list(arr)  # 원본 리스트 복사
    min_num = min(original_list)  # 배열에서 가장 작은 수 찾기
    original_list.remove(min_num)  # 가장 작은 수 제거

    return original_list  # 수정된 리스트 반환