function solution(n) {
let answer = 0;
if (n <= 7) {
    answer++;
} else {
    answer = n / 7;
    if (answer % 1 !== 0) {
        answer++;
    }
}
console.log(Math.floor(answer));
return Math.floor(answer);
}