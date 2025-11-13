function solution(my_string) {
    var answer = '';
    
    for (let i = 0; i < my_string.length; i++) {
        const char = my_string[i];
        
        if (!answer.includes(char)) {
            answer += char;
        }
    }
    return answer;
}