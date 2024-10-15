def solution(money):
    answer = []
    ice_coffee = 5500
    answer.append(money // ice_coffee)
    answer.append(money % ice_coffee)
    print(answer)
    return answer