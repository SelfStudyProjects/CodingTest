// 1. A와 B가 이미 같은지 먼저 확인 (밀지 않아도 같은 경우: 0번 이동)

// 2. A를 문자열에서 배열로 변환 (pop, unshift를 활용하기 위함)
//    Array.from() 또는 스프레드 문법 [...]을 사용할 수 있습니다.

// 3. A의 길이 (즉, 몇 번까지 밀어볼 수 있는지 최대 횟수)
//    이 길이만큼 밀면 다시 원래 A의 상태로 돌아오게 됩니다.

// 4. 문자열을 민 횟수를 저장할 변수 (0번 민 경우는 이미 위에서 처리했으므로)

// 5. numShifts (A의 길이)만큼 반복하며 한 칸씩 밀어봅니다.
//    for (let i = 0; i < numShifts; i++) 도 가능합니다.

// 한 칸 밀었으니 횟수 증가

// - pop()을 활용해서 맨 뒤 요소 제거
//   js의 pop()은 제거된 요소를 반환합니다.
// - unshift()를 활용해서 새로운 요소 (제거된 마지막 요소)를 맨 앞에 추가
// 위 과정들을 수행 후, 현재 listA가 B와 같은지 비교
// 배열을 문자열로 다시 합쳐서 비교해야 합니다.
// 같으면 현재까지 민 횟수 반환
// for 반복문 다 수행했는데 동일한 값이 없으면 (즉, 위에서 return 되지 않으면)
// -1 반환

function solution(A, B) {
    if (A === B) {
        return 0;
    }
    let listA = Array.from(A); 
    const numShifts = A.length; 
    
    let shiftCount = 0; 
    for (let i = 0; i < numShifts; i++) {
        shiftCount++;
        const lastChar = listA.pop(); 
        
        listA.unshift(lastChar); 
        if (listA.join('') === B) {
            return shiftCount;
        }
    }
    return -1;
}