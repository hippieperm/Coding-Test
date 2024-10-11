class Solution {
    fun solution(numLog: IntArray): String {
       var answer = ""
for (i in 1 until numLog.size) {
    val difIndex = numLog[i] - numLog[i - 1]
    when (difIndex) {
        1 -> answer += "w"
        -1 -> answer += "s"
        10 -> answer += "d"
        -10 -> answer += "a"
    }
}
println("wri")
println(answer)
return answer
    }
}