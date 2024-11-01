
function solution(x, n) {
    let answer = [];
    let cnt = 0;
    for (let i = x; cnt < n; i += x) {
        answer.push(i);
        cnt++;
    }
    console.log(answer);
    return answer;
}
