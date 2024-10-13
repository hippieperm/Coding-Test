function solution(array) {
    let answer = 0;
let centerVal = Math.floor(array.length / 2);
array.sort((a, b) => a - b);
for (let i = 0; i <= centerVal; i++) {
    answer = array[i];
}
return answer;
}