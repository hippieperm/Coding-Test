function solution(array, n) {
let answer = 0;
for (let index of array) {
    if (index === n) answer++;
}
return answer;
}