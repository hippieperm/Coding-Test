def solution(arr1, arr2):
    answer = 0
    length1 = len(arr1)
    length2 = len(arr2)

    arrVar1 = 0
    arrVar2 = 0

    if length1 != length2:
        answer = 1 if length1 > length2 else -1
    else:
        for i in range(length1):
            arrVar1 += arr1[i]
            arrVar2 += arr2[i]
        answer = 1 if arrVar1 > arrVar2 else -1 if arrVar1 < arrVar2 else 0

    return answer