/*
 * [트러블슈팅] 문자열 뒤집기 문제 - TypeError: ~.join is not a function
 *
 * 문제 현상:
 *   `final_string.join('')` 에서 `TypeError` 발생.
 *   `final_string` 변수에는 `join()` 함수가 없다는 메시지.
 *
 * 원인 분석:
 * 1.  `join()` 메서드는 **배열 전용** 함수임. (문자열에는 없음.)
 * 2.  `const final_string = reversed_string.toString();` 코드 때문에,
 *     `reversed_string` 배열이 **쉼표(,)가 포함된 "문자열"**로 변환되어 `final_string`에 할당됨.
 * 3.  결과적으로, 문자열인 `final_string`에 배열 메서드인 `join()`을 호출하여 에러 발생.
 *
 * 해결 방법:
 *   `toString()` 변환 없이, **배열인 `reversed_string`에 직접 `join('')`을 호출**하여
 *   문자들을 하나의 문자열로 합침.
 *
 * 코드 수정 요약:
 *   `const final_string = reversed_string.toString();` (삭제 또는 주석처리)
 *   `const result = final_string.join('');`  ➡️  `const result = reversed_string.join('');` (수정)
 *
 * 추가 조언 (코드 가독성 향상):
 *   `for (let x in array)` (for...in 루프) 대신 `for (let x of array)` (for...of 루프)를 사용하면
 *   배열의 요소 값을 직접 얻을 수 있어 코드가 더 명확해짐.
 *
 */

function solution(my_string) {
    const origin_string = my_string.split('')
    const reversed_string = []
    for (letter in origin_string){
        reversed_string.unshift(origin_string[letter])
    }
    const result = reversed_string.join('')
    return result;
}