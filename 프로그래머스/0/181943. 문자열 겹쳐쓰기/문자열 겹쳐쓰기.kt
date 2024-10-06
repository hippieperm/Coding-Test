class Solution {
fun solution(myString: String, overwriteString: String, s: Int): String {
    var answer = myString.substring(0, s) + overwriteString
    answer += myString.substring(answer.length)
    return answer
}
}