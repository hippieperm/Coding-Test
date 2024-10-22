def solution(s1, s2):
    answer = 0
    for element in s1:
        for i in range(len(s2)):
            print(s2[i])
            if element == s2[i]:
                answer += 1
    print(answer)
    return answer