// 내 풀이
function solution(num1, num2) {
    var answer = Math.floor(num1 / num2) ;
    return answer;
}

// 김호준 T 풀이
// '~' : 보수를 나타내는 기호, '~~'를 이용하면 floor와 똑같은 기능 구현 가능
function solution(num1, num2) {
    var answer = ~~(num1 / num2);
    return answer;
}