class Solution {
    fun solution(myString: String, k: Int): String {
        var answer = ""
        for (i in 0 until k) {
            answer += myString
        }
        return answer
    }
}