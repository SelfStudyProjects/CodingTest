/*
다시 ㄱㄱ 

설명: 정수 n(0 이상)이 주어질 때, n번째 피보나치 수 fib(n)을 재귀 + 메모이제이션으로 계산하는 함수를 작성하세요.

피보나치 정의: fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2) (n ≥ 2)
반환 타입: JavaScript Number (주의: 엄청 큰 n에 대해서는 오버플로/정밀도 한계 존재)
제한사항

0 ≤ n ≤ 10_000
재귀 깊이로 인해 매우 큰 n(예: 몇만)은 스택오버플로우가 발생할 수 있음 — 그런 경우 바텀업(반복) 방식 권장
memo(캐시)는 함수 내부 해시맵(object 또는 Map) 형태로 사용
기본 매개변수로 빈 객체를 그대로 쓰면 호출들 사이에 공유될 수 있어 주의 (권장: memo === undefined 체크로 초기화)
입출력 예

입력: n = 10 → 출력: 55
입력: n = 0 → 출력: 0
입력: n = 1 → 출력: 1
*/

// fibMemo: 재귀 + 메모이제이션
// 주의: memo 기본값으로 {}를 직접 사용하면 함수를 여러 번 호출할 때 의도치 않게 공유될 수 있음.
// 따라서 아래 템플릿처럼 memo === undefined 체크 방식 권장.

function fibMemo(n, memo) {
  if (typeof n !== 'number' || n < 0 || !Number.isInteger(n)) {
    throw new Error('n은 0 이상의 정수여야 합니다.');
  }

  // 안전한 초기화: 기본 매개변수로 {}를 바로 쓰면 공유 이슈가 있으므로 내부에서 처리
  if (memo === undefined) memo = {};

  // 캐시 검사: 이미 계산해둔 값이 있으면 즉시 반환
  if (memo.hasOwnProperty(n)) return memo[n];

  // 기저 조건: n이 0 또는 1이면 그 값을 반환
  if (n <= 1) {
    memo[n] = n;
    return n;
  }

  // 재귀로 하위 문제 계산 (memo를 계속 전달)
  const val = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);

  // 계산 결과를 캐시에 저장하고 반환
  memo[n] = val;
  return val;
}

/*
console.log(fibMemo(0));   // 0
console.log(fibMemo(1));   // 1
console.log(fibMemo(2));   // 1
console.log(fibMemo(10));  // 55
console.log(fibBottomUp(10)); // 55
*/