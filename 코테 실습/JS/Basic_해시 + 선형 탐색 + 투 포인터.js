/*
문제 요약

Part A (Two-Sum Indices): 정수 배열 arr와 정수 target이 주어질 때, arr에서 합이 target인 두 수의 인덱스(0-based)를 반환하라. 없으면 [-1, -1]. 동일 값이 여러 번 있을 수 있으니 인덱스 처리에 주의할 것.
Part B (Longest Subarray Sum ≤ S): 비음수 원소로 이루어진 정수 배열 arr와 정수 S가 주어질 때, 합이 S 이하인 가장 긴 연속 부분배열의 길이를 반환하라.
제한사항(공통)

1 ≤ arr.length ≤ 100,000
배열 원소는 정수(Part B는 비음수 가정)
시간복잡도 목표: 각 파트 O(n)
메모리: Part A는 O(n) 해시, Part B는 O(1) 추가 공간
입출력 예 (정정된 예시)

Part A: arr = [2,7,11,15], target = 9 → [0,1]
Part A: arr = [3,3], target = 6 → [0,1]
Part B: arr = [1,2,1,0,1,1,0], S = 3 → 정답 length = 5 (예: [1,0,1,1,0], 인덱스 2..6)
*/

/*
Map 함수 :
의미 -> 반복 가능한(iterable) 객체(배열, 리스트 등)의 각 요소에 지정된 함수를 적용하여 변환하고,
그 결과를 담은 새로운 컬렉션(배열/리스트)을 만들어 반환하는 기능

구체적인 기능 -> 리스트, 튜플 등 여러 개의 데이터를 입력받아 각 요소에 함수를 적용한 결과를 묶어 반환합니다.
예시: map(함수, 리스트) 형태로, 리스트의 모든 숫자를 2배로 만들거나, 문자열을 대문자로 바꾸는 등의 작업을 할 때 사용됩니다.

*/

function twoSumIndices(arr, target) {
  const map = new Map(); // value -> earliest index
  for (let i = 0; i < arr.length; i++) {
    const val = arr[i];
    const need = target - val;
    if (map.has(need)) {
      return [map.get(need), i];
    }
    if (!map.has(val)) map.set(val, i);
  }
  return [-1, -1];
}

// Part B: longest subarray with sum <= S (non-negative numbers)
function longestSubarrayAtMostS(arr, S) {
  let left = 0;
  let sum = 0;
  let maxLen = 0;

  for (let right = 0; right < arr.length; right++) {
    sum += arr[right];

    // sum이 S 초과이면 left를 옮겨 합을 줄인다
    while (sum > S && left <= right) {
      sum -= arr[left];
      left++;
    }

    // 현재 윈도우 길이 갱신
    maxLen = Math.max(maxLen, right - left + 1);
  }

  return maxLen;
}