class Solution {
    fun solution(a: Int, b: Int): Int {
    var answer = 0

    val calInt = "$a$b".toInt()
    val cal2 = 2 * a * b

    if (calInt > cal2) {
        return calInt
    }
    if (calInt < cal2) {
        return cal2
    }
    if (calInt == cal2) {
        answer = calInt
    }
    return answer
}
}