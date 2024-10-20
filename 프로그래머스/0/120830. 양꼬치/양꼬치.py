def solution(n, k):
    answer = 0
    sheepNiku = 12000 * n
    allCoke = k * 2000

    disCoke = (sheepNiku // 120000) * 2000

    if disCoke >= 2000:
        answer += allCoke - disCoke
        answer += sheepNiku
    else:
        answer += sheepNiku
        answer += allCoke

    print(answer)
    return answer