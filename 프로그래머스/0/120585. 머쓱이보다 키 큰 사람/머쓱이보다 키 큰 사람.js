function solution(array, height) {
   let answer = 0;
for (let element of array) {
    if (element > height) answer++;
}
return answer;
}