def solution(myString, s, e):
    split_str = myString[s:e+1]
    end_str = myString[e+1:]
    answer = myString[:s] + split_str[::-1] + end_str
    return answer