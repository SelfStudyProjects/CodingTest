function solution(my_string) {
    var answer = ''; // 최종 결과를 담을 문자열. 중복 제거된 문자들이 여기에 추가됨.
    
    // ⭐ 수정 1: my_string.length (오타 수정)
    // ⭐ 수정 2: 'let i'로 변수 선언
    for (let i = 0; i < my_string.length; i++) {
        const char = my_string[i]; // 현재 반복 중인 문자 (가독성을 위해 변수에 저장)
        
        // ⭐ 수정 3: if (answer.includes(char)) 로직 변경! ⭐
        // 'answer' 문자열에 'char'가 이미 포함되어 있지 않다면 (파이썬의 'char not in answer'와 동일)
        if (!answer.includes(char)) { // !는 '부정'을 의미. 즉, 'answer에 char가 포함되어 있지 않다면'
            answer += char; // answer에 해당 문자를 추가
        }
    }
    return answer; // 중복 제거된 문자열 반환
}