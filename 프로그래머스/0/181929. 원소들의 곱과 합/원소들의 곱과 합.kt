class Solution {
    fun solution(num_list: IntArray): Int {
        var mix: Long = 1
        var sum: Long = 0
        for (num in num_list) {
            sum += num.toLong()
            mix *= num.toLong()
        }
        return if (sum * sum > mix) 1 else 0
    }
}