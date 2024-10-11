class Solution {
    fun solution(n: Int, control: String): Int {
       var answer = n
for (i in control.indices) {
    val index = control[i]
    when (index) {
        'w' -> answer++
        's' -> answer--
        'd' -> answer += 10
        'a' -> answer -= 10
    }
}
println(answer)
return answer
    }
}