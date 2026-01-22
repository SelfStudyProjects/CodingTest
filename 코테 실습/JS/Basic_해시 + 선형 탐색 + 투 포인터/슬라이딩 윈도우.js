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

// Part A: two-sum using Map
function twoSumIndices(arr, target) {
  // Map to store value -> index mapping
  const map = new Map();
  
  // Iterate through array
  for (let i = 0; i < arr.length; i++) {
    const complement = target - arr[i];
    
    // Check if complement exists in map
    if (map.has(complement)) {
      // Found pair: return indices in order
      return [map.get(complement), i];
    }
    
    // Store current value and its index
    map.set(arr[i], i);
  }
  
  // No solution found
  return [-1, -1];
}

// Part B: longest subarray with sum <= S (non-negative numbers)
function longestSubarrayAtMostS(arr, S) {
  // TODO: implement sliding window / two pointers
}