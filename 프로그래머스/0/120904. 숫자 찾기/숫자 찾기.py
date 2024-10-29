def solution(num, k):
    num_str = str(num)
    k_str = str(k)

    if k_str in num_str:
        for i in range(len(num_str)):
            if num_str[i] == k_str:
                return i + 1
    return -1