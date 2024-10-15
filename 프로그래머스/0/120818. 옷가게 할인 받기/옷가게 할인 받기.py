def solution(price):
    five_percentage = 0.95
    ten_percentage = 0.90
    twenty_percentage = 0.80

    if price >= 500000:
        answer = int(price * twenty_percentage)
    elif price >= 300000:
        answer = int(price * ten_percentage)
    elif price >= 100000:
        answer = int(price * five_percentage)
    else:
        answer = price

    print(answer)
    return answer