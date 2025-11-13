// 다시 풀기
// 생성 예시는 아래 주석들과 같습니다.

/*
numbers	result
"onetwothreefourfivesixseveneightnine"	123456789
"onefourzerosixseven"	14067
*/

/*
Object.entries(obj)
객체 ==> 배열 :
객체를 배열로 만들어 준다.
객체의 키와 값을 [key, value]의 배열(딕셔너리)로 반환한다.
(객체가 배열로 바뀜에 따라 key와 value는 순서성을 가지게 됨)

Object.fromEntries(arr)
배열(딕셔너리) ==> 객체 :
2차원으로 구성된 배열의 키 값 쌍 목록을 객체로 바꾼다.
*/

function solution(numbers) {

    const numMap = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    };

    let resultStr = ""; // 빈 문자열 생성
    let currentIdx = 0; // numbers 배열에서 요소의 인덱스를 나타냄

    while (currentIdx < numbers.length) {
        let foundMatch = false;

        for (const [word, digit] of Object.entries(numMap)) {
            // 그 객체 안에 있는 모든 키-값 쌍을 **[키, 값] 형태의 '배열' 요소들로 이루어진 '배열'**로 바꿔줘.
            // 배열, 문자열, Map, Set 같은 "반복 가능한(iterable)" 자료형으로 for 반복문을 시행할 수 있음
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