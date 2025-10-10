/* 
첫번째, sorted를 해서 리스트업(내림차순)을 하기
두번째, 리스트업된 리스트의 인덱스를 기준으로 replace 함수 쓰는 건 어떨까?

참고_1 : 배열의 각 요소에 대해 지정된 함수를 실행하고, 그 결과를 모아 새로운 배열로 반환
*/

function solution(emergency) {
    const sortedEmergency = [...emergency].sort((a, b) => b - a);
    
    const answer = emergency.map(value => {
        // 3. 각 원본 값이 내림차순 정렬 배열에서 몇 번째인지 인덱스 검색 후 1 더하기
        return sortedEmergency.indexOf(value) + 1;
    });

    return answer;
}