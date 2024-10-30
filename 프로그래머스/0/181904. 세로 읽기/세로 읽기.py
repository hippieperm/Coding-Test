def solution(myString, m, c):
    answer = ''
    list_2d = [
        [''] * m for _ in range((len(myString) + m - 1) // m)
    ]

    for i in range(len(myString)):
        list_2d[i // m][i % m] = myString[i]
    for row in list_2d:
        if c - 1 < m:
            answer += row[c - 1]
    return answer