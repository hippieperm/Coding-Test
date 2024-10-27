def solution(myString, isPrefix):
    str_ = ''
    for element in myString:
        str_ += element
        if str_ == isPrefix:
            return 1
    return 0