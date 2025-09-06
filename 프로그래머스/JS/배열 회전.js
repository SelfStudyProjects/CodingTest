function solution(numbers, direction) {
    // 💡 참고: JavaScript에서 배열 복사본을 만들어두는 것이 좋은 습관일 때가 있어.
    // 여기서는 원본 배열을 변경해도 문제 없으므로 그대로 진행!

    if (direction === "right") {
        // 오른쪽으로 회전: 배열의 마지막 요소를 꺼내서 맨 앞에 넣기
        // 1. 배열의 마지막 요소를 제거하고 그 값을 가져와
        const lastElement = numbers.pop(); // numbers는 이제 마지막 요소가 없어진 상태
        // 2. 가져온 마지막 요소를 배열의 맨 앞에 추가해
        numbers.unshift(lastElement); // numbers는 이제 맨 앞에 lastElement가 추가된 상태
    } else { // direction === "left"
        // 왼쪽으로 회전: 배열의 첫 번째 요소를 꺼내서 맨 뒤에 넣기
        // 1. 배열의 첫 번째 요소를 제거하고 그 값을 가져와
        const firstElement = numbers.shift(); // numbers는 이제 첫 번째 요소가 없어진 상태
        // 2. 가져온 첫 번째 요소를 배열의 맨 뒤에 추가해
        numbers.push(firstElement); // numbers는 이제 맨 뒤에 firstElement가 추가된 상태
    }

    // 회전이 완료된 numbers 배열을 반환
    return numbers;
}