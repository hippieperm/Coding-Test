def solution(slice, n):
    min_pizza = n // slice
    if n % slice != 0:
        min_pizza += 1
    return min_pizza