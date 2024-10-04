class Solution {
    fun solution(age: Int): Int {
    var answer = 0
    if (age in 1..120) {
        answer = (2022 - age) + 1
    }
    return answer
}
}