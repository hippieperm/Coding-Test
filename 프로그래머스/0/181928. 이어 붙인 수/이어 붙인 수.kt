class Solution {
    fun solution(numlist: IntArray): Int {
       var even = ""
var odd = ""

for (num in numlist) {
    val strNum = num.toString()
    if (num % 2 == 0) {
        even += strNum
    } else {
        odd += strNum
    }
}
val intEven = even.toInt()
val intOdd = odd.toInt()
println(intOdd + intEven)
return intOdd + intEven
    }
}