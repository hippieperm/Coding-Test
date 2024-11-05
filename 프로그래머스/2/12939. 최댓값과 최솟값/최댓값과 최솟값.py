def solution(s):
    lst = []
    for element in s.split(' '):
        lst.append(int(element))
    lst.sort()
    min_value = min(lst)
    max_value = max(lst)

    return f'{min_value} {max_value}'