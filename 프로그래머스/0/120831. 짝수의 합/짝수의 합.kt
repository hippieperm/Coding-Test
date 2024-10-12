class Solution {
    fun solution(n: Int): Int {
  var answer = 0
for (i in 2..n step 2) {
    answer += i
}
println(answer)
return answer
    }
}