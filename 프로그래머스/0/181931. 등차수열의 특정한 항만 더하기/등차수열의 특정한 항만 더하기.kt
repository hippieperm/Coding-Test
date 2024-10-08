class Solution {
    fun solution(num1: Int, d: Int, included: BooleanArray): Int {
        var answer = 0
        var a = num1
        for (bool in included) {
            if (bool) {
                answer += a
            }
            a += d
        }
        return answer
    }
}