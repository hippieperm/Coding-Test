def solution(rnyString):
    answer = ""
    for element in rnyString:
        answer += "rn" if element == "m" else element
    return answer