class Solution {
    fun solution(numList: IntArray): IntArray {
        val lastVal = numList[numList.size - 1]
        val minusoneVal = numList[numList.size - 2]
        val listInstances = if (lastVal > minusoneVal) {
            lastVal - minusoneVal
        } else {
            lastVal * 2
        }

        // 새로운 IntArray 생성
        return numList + intArrayOf(listInstances)
    }
}