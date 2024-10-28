def solution(my_strings, parts):
    answer = ""
    for i in range(len(my_strings)):
        index = parts[i]
        if (index[0] < len(my_strings[i]) and
            index[1] <= len(my_strings[i]) and
            index[0] <= index[1]):
            answer += my_strings[i][index[0]:index[1] + 1]
    return answer