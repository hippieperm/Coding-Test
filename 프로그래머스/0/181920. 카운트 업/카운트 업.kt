class Solution {
   fun solution(startNum: Int, endNum: Int): List<Int> {
    val answer = mutableListOf<Int>()
    for (i in startNum..endNum) {
        answer.add(i)
    }
    println(answer)
    return answer
}
}