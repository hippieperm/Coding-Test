def solution(myString, letter):
    answer = ''
    for element in myString:
        if letter != element:
            answer += element
    print(answer)
    return answer