class Solution {
fun solution(myString: String, isSuffix: String): Int {
    var answer = 0
    for (i in myString.indices) {
        val subMyString = myString.substring(i, myString.length)
        if (subMyString == isSuffix) {
            return 1
        }
    }
    return answer
}
}