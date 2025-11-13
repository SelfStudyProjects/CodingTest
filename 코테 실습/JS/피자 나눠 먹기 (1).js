function solution(n) {
    var answer = 0;
    if (n % 7 != 0){
        answer += 1
    }
    x = Math.floor(n / 7)
    answer += x
    return answer;
}