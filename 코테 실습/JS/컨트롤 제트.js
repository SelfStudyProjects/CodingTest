// # s를 list로 변형, 공백을 기준으로 split() 메서드 활용
// # s.split()은 기본적으로 공백 기준으로 분리
// 공백 기준으로 문자열을 배열로 분리
// # 최종 결과값 시작값 설정, x=0 (answer 대신 totalSum을 사용할게요!)
// # Z가 나왔을 때, '바로 직전에 더했던 숫자'를 저장할 스택
// # 파이썬 리스트는 스택처럼 사용할 수 있습니다.
// 자바스크립트에서도 배열(Array)이 스택처럼 사용할 수 있습니다 (push와 pop 메서드 활용).
// # for 반복문 이용하기, sList의 각 요소를 순회합니다.
// # if문 활용해서, Z인지 여부에 이분법적으로 분류
// # Z라면: numStack에 숫자가 있을 경우에만 가장 최근에 더했던 숫자를 뺌
// # 스택이 비어있지 않다면 (스택에 뭔가 있다면)
// # 스택에서 가장 최근 숫자 제거 (pop 메서드는 배열의 마지막 요소를 제거하고 반환)
// # 제거된 숫자를 totalSum에서 댐
// 문자열 "10"을 숫자 10으로 변환
// # totalSum에 현재 숫자 더함 
// # for 반복문 끝나면 최종값 totalSum 반환 

function solution(s) {
    const sList = s.split(' ');

    let totalSum = 0;
    const numStack = [];

    for (const item of sList) {
        if (item === "Z") {
            if (numStack.length > 0) { // numStack에 요소가 있을 때만 하려는 의도
                const poppedNum = numStack.pop(); 
                totalSum -= poppedNum;
            }
        } else {
            const num = Number(item);
            totalSum += num;           
            numStack.push(num);      
        }
    }
    return totalSum;
}