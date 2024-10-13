class Solution {
    fun solution(num_list: IntArray): IntArray {
        var even = 0
        var odd = 0
        // num_list를 numList로 변경
        for (nl in num_list) {
            if (nl % 2 == 0) {
                even += 1
            } else {
                odd += 1
            }
        }
        // MutableList 대신 IntArray 사용
        return intArrayOf(even, odd)
    }
}