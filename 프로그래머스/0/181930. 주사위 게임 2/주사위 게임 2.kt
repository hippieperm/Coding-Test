class Solution {
fun solution(a: Int, b: Int, c: Int): Int {
    var answer = 0
    if (a != b && b != c && a != c) {
        answer = a + b + c
    }
    if (a == b || b == c || a == c) {
        answer = (a + b + c) * ((a * a) + (b * b) + (c * c))
    }
    if (a == b && b == c) {
        answer = (a + b + c) *
                 ((a * a) + (b * b) + (c * c)) *
                 ((a * a * a) + (b * b * b) + (c * c * c))
    }
    return answer
}
}