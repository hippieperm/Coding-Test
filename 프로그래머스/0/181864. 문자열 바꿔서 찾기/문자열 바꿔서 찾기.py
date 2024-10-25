def solution(myString, pat):
    answer = 0
    trans = ""
    for element in myString:
        trans += "B" if element == "A" else "A"
        answer = 1 if pat in trans else 0
    return answer