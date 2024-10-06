class Solution {
fun solution(a: Int, b: Int): Int {
    val sum1 = "$a$b".toInt()
    val sum2 = "$b$a".toInt()

    return if (sum1 >= sum2) sum1 else sum2
}
}