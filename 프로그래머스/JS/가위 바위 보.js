// 가위바위보 파일 생성

>>>>>>> 7df5946686d25d21ac8f151e491bf58b64837188
function solution(rsp) {
    var answer = '';
    for(let i = 0; i < rsp.length; i++){
        if(rsp[i] === '2'){
            answer += '0'
        }
        else if(rsp[i] === '0'){
            answer += '5'
        }
        else{
            answer += '2'
        }
    }
    return answer;
}