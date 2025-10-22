/*
# A와 B를 문자열을 배열로 변환시켜주기, array.from() 함수 활용
# A를 기준으로 length해서 전체 요소 개수, n으로 두기
# n을 기준으로 for 반복문 시행
# n은 for 반복문 시행되기 전에 0으로 설정
# if문 두기, A와 B 같은지 먼저 비교 후 같으면 result 0, 아니면 for 반복문으로 가는 로직
# for 반복문 시행 동안 아래 내용들 수행
# - pop()을 활용해서 맨 뒤 요소 제거, 그리고 따로 inserted_chr로 문자를 받기
# - unshift()를 활용해서 새로운 요소 추가하기
# - 시행 횟수 n += 1 하기
# - 위 과정들을 수행 후 B와 비교, 같으면 break 해서 retrun n 하기
# 만일 for 반복문 다 수행했는데 동일한 값이 없으면 result -1 하기
*/

function solution(A, B) {
    // 1. A와 B가 이미 같은지 먼저 확인 (밀지 않아도 같은 경우: 0번 이동)
    if (A === B) {
        return 0;
    }

    // 2. A를 문자열에서 배열로 변환 (pop, unshift를 활용하기 위함)
    //    Array.from() 또는 스프레드 문법 [...]을 사용할 수 있습니다.
    let listA = Array.from(A); 
    
    // 3. A의 길이 (즉, 몇 번까지 밀어볼 수 있는지 최대 횟수)
    //    이 길이만큼 밀면 다시 원래 A의 상태로 돌아오게 됩니다.
    const numShifts = A.length; 
    
    // 4. 문자열을 민 횟수를 저장할 변수 (0번 민 경우는 이미 위에서 처리했으므로)
    let shiftCount = 0; 

    // 5. numShifts (A의 길이)만큼 반복하며 한 칸씩 밀어봅니다.
    //    for (let i = 0; i < numShifts; i++) 도 가능합니다.
    for (let i = 0; i < numShifts; i++) {
        shiftCount++; // 한 칸 밀었으니 횟수 증가

        // - pop()을 활용해서 맨 뒤 요소 제거
        //   js의 pop()은 제거된 요소를 반환합니다.
        const lastChar = listA.pop(); 
        
        // - unshift()를 활용해서 새로운 요소 (제거된 마지막 요소)를 맨 앞에 추가
        listA.unshift(lastChar); 
        
        // 위 과정들을 수행 후, 현재 listA가 B와 같은지 비교
        // 배열을 문자열로 다시 합쳐서 비교해야 합니다.
        if (listA.join('') === B) {
            return shiftCount; // 같으면 현재까지 민 횟수 반환
        }
    }

    // for 반복문 다 수행했는데 동일한 값이 없으면 (즉, 위에서 return 되지 않으면)
    return -1; // -1 반환
}