def solution(hp):
    generalAntVal = hp // 5
    generalAntRemainder = hp % 5

    soldierAntVal = generalAntRemainder // 3
    soldierAntRemainder = generalAntRemainder % 3

    workerAntVal = soldierAntRemainder // 1

    return generalAntVal + soldierAntVal + workerAntVal