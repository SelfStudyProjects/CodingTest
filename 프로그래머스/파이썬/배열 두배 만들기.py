'''
 * [트러블슈팅] TypeError: insert expected 2 arguments, got 1
 *
 * 문제 현상:
 *   `answer.insert(num)` 코드에서 `TypeError` 발생.
 *   `insert()` 함수는 2개의 인자(arguments)를 기대하는데 1개만 받았다는 메시지.
 *
 * 원인 분석:
 * 1.  파이썬의 `insert()` 메서드는 리스트의 **특정 위치(인덱스)에 요소를 삽입**하는 함수임.
 * 2.  따라서 `insert()`는 반드시 `insert(index, element)`와 같이 **두 개의 인자**를 받아야 함.
 *     - 첫 번째 인자: 삽입할 '인덱스' (위치)
 *     - 두 번째 인자: 삽입할 '요소' (값)
 * 3.  제출된 코드에서는 `answer.insert(num)`처럼 '삽입할 요소'인 `num`만 전달했고, '인덱스' 인자가 누락되었기 때문에 에러 발생.
 *
 * 해결 방법:
 *   리스트의 **맨 뒤에 요소를 추가**하는 것이 목적이므로, 인자 하나만 받는 `append()` 메서드를 사용해야 함.
 *
 * 코드 수정 요약:
 *   `answer.insert(num)`  ➡️  `answer.append(num)` (수정)
 *
 */
'''

def solution(numbers):
    answer = []
    for num in numbers:
        num *= 2
        answer.append(num)
    return answer