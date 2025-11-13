function solution(array, n) {
    var answer = 0;
    for (let x = 0; x < array.length; x++){
        if (array[x] === n){
            answer += 1
        }
    }
    return answer
}