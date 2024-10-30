def solution(binomial):
    if '+' in binomial:
        str_list = binomial.split(' + ')
        int_list = list(map(int, str_list))
        answer = int_list[0] + int_list[1]
    elif '*' in binomial:
        str_list = binomial.split(' * ')
        int_list = list(map(int, str_list))
        answer = int_list[0] * int_list[1]
    elif '-' in binomial:
        str_list = binomial.split(' - ')
        int_list = list(map(int, str_list))
        answer = int_list[0] - int_list[1]
    return answer