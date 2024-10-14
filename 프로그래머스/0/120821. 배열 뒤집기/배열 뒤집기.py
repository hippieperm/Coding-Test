
def solution(num_list):
    answer = []
    for i in range(len(num_list) - 1, -1, -1):
        answer.append(num_list[i])
        # print(answer[i])  # 이거 확인
        if i == 0:
            break
    print(answer)
    return answer