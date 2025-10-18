// 다시 풀기

function solution(numbers) {

    const numMap = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    };

    let resultStr = "";
    let currentIdx = 0;

    while (currentIdx < numbers.length) {
        let foundMatch = false;

        for (const [word, digit] of Object.entries(numMap)) {
            // 현재 numbers 문자열의 'currentIdx' 위치부터 'word'와 일치하는지 확인
            if (numbers.startsWith(word, currentIdx)) {
                resultStr += digit;       // 일치하면 해당 숫자를 resultStr에 추가
                currentIdx += word.length;  // numbers 문자열에서 해당 영문 숫자만큼 처리 위치를 이동
                foundMatch = true;        // 매칭되는 단어를 찾았음을 표시
                break;                    // 현재 위치에서 하나의 영문 숫자를 찾았으니 다음 위치로 이동
            }
        }
        
        // (이 문제는 모든 숫자가 영문으로 변환 가능하므로 이 if 블록에 도달할 일은 없을 것입니다.
        //  하지만 '없을 때는 반복 중단'이라는 원래 의도를 반영하기 위한 방어적 코드입니다.)
        if (!foundMatch) {
            // 예상치 못한 상황 (numbers에 numMap에 없는 단어가 있는 경우 등)
            // 여기서는 문제 제한사항 때문에 실제로 작동할 일은 없으나,
            // 더 범용적인 로직이라면 처리 필요. 이 문제에서는 break 또는 error 처리 가능.
            break; 
        }
    }
    
    // 최종 결과 문자열을 정수로 변환하여 반환
    return Number(resultStr); // 또는 parseInt(resultStr, 10);
}