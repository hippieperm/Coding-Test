def solution(myString, pat):
    str_lower = myString.lower()
    pat_lower = pat.lower()
    return 1 if pat_lower in str_lower else 0