function solution(my_str, n) {
    var answer = [];
    let length = my_str.length;
    for (let i = 0; i < length; i += n) {
        answer.push(my_str.slice(i, i + n));
    }
    return answer;
}
