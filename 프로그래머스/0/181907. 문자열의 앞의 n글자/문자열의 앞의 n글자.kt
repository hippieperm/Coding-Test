class Solution {
  fun solution(myString: String, n: Int): String {
    var answer = ""
    for (i in 0 until n) {
        answer += myString[i]
    }
    return answer
}
}