def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

print(linear_search([5, 3, 2, 8], 2))  # 2

'''
1) 선형 탐색 (Linear Search)
문제 설명
정수로 이루어진 배열 arr과 정수 target이 주어질 때, arr에서 target이 처음 등장하는 인덱스를 반환하세요. 만약 배열에 target이 없다면 -1을 반환하세요.

제한사항(예시)

0 ≤ len(arr) ≤ 10^5 (실제 환경에 따라 달라짐)
arr의 원소와 target은 정수
입출력 예

arr = [5, 3, 2, 8], target = 2 → result = 2
arr = [1, 2, 3], target = 4 → result = -1

라인별 why — how — what 설명

# def linear_search(arr, target):

what: arr와 target을 입력으로 받는 함수 정의.
why: 같은 동작을 여러 번 쓰거나 테스트할 때 재사용하려고 함수로 만듦.
how: 파이썬의 함수 선언 문법을 사용해 이름과 매개변수 지정.

# for i, val in enumerate(arr):

what: 배열을 앞에서부터 순서대로 순회하면서 인덱스(i)와 값(val)을 동시에 얻음.
why: 찾으면 그 인덱스를 반환해야 하므로 인덱스가 필요함. 또한 순차 탐색이므로 모든 원소를 검사해야 함.
how: enumerate를 사용하면 코드가 간결해짐(인덱스와 값을 별도로 관리할 필요 없음).

# if val == target:

what: 현재 검사 중인 원소가 target과 동일한지 비교.
why: 같으면 탐색 성공이므로 즉시 인덱스를 반환하여 추가 검사 낭비를 막음.
how: == 연산자로 비교.

# return i

what: 찾은 위치(인덱스)를 반환하고 함수 종료.
why: 함수의 목적을 달성(찾은 위치 제공).
how: 파이썬의 return 문 사용.

# return -1

what: 루프 종료 후에도 찾지 못한 경우 -1 반환.
why: 찾지 못했음을 명시적으로 표현(관례).
how: 루프 바깥에 위치해 전체 검사가 끝난 뒤 실행됨.

알고리즘/자료구조 구체적 설명 — 선형 탐색

정의: 배열의 처음부터 끝까지 각 원소를 하나씩 검사해 target을 찾는 탐색 기법.
시간복잡도: 최선 O(1) (첫 원소가 target인 경우), 평균/최악 O(n).
공간복잡도: O(1) — 추가 메모리 거의 없음.
장점: 구현 간단, 정렬 필요 없음.
단점: 최악의 경우 모든 원소를 검사해야 하므로 큰 입력에 비효율적.
실제 적용 팁:
빈 리스트나 중복값을 고려한 테스트 케이스 작성.
다수 조회가 예상되면 해시 기반 구조(set/dict)로 변경해 평균 조회 O(1)를 노릴 것(단, 인덱스를 반환해야 하면 추가 설계 필요).
'''