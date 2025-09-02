function solution(numbers) {
    var answer = [];
    for (num in numbers){
        double_num = numbers[num] * 2
        answer.push(double_num)
    }
    return answer;
}