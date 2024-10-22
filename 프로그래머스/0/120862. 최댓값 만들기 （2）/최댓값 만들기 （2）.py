def solution(numbers):
    max_product = -99999999999999999999999999

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            num = numbers[i] * numbers[j]
            if num >= max_product:
                max_product = num

    print(max_product)
    return max_product