def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(10))  # 55

'''
좀 더 안전된 버전은 아래와 같습니다.
'''

def fib(n, memo=None):
    if memo is None:  # ★ 함수가 호출될 때마다 새로운 딕셔너리를 생성
        memo = {}
        
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
        
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

'''
이 방식은 fib 함수를 프로그램 내에서 수십 번 호출하더라도, 각 호출마다 완전히 독립된 빈 딕셔너리로 시작하기 때문에 안전합니다.

memo={}와 같이 가변(Mutable) 객체(list, dict 등)를 기본 인자로 사용하면, 이 객체는 함수가 정의될 때 (compile time) 딱 한 번만 생성
만약 memo에 잘못된 값이 저장되어 있었다면 버그가 됩니다.

결론: 원본 코드는 파이썬의 가변 기본 인자 규칙에 대한 흔한 실수이지만,
코딩 테스트 환경(대부분의 경우 함수를 딱 한 번만 실행함)에서는 큰 문제가 되지 않아 종종 사용되기도 합니다.
하지만 클린 코드와 재사용성을 위해서는 memo=None 패턴을 사용하는 것이 훨씬 안전하고 바람직합니다.
'''

'''
문제 설명
정수 n이 주어질 때, n번째 피보나치 수를 반환하세요. (피보나치 정의: fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2) for n≥2)

제한사항(예시)

0 ≤ n ≤ 10^4 (큰 n의 경우 시간/메모리 고려 필요)
결과는 정수 (매우 큰 수의 경우 모듈러 연산을 요구할 수도 있음)
입출력 예

n = 10 → result = 55
n = 0 → result = 0
n = 1 → result = 1

fib(2) = fib(1) + fib(0) = 1 + 0 = 1
fib(3) = fib(2) + fib(1) = 1 + 1 = 2
fib(4) = fib(3) + fib(2) = 2 + 1 = 3
fib(5) = fib(4) + fib(3) = 3 + 2 = 5
fib(6) = fib(5) + fib(4) = 5 + 3 = 8
등등

라인별 why — how — what 설명

def fib(n, memo={}):

what: n번째 피보나치 수를 계산하는 함수. memo는 계산한 값을 저장하는 캐시(딕셔너리).
why: 동일한 하위 문제를 여러 번 계산하는 것을 방지하기 위해 메모(캐시)를 사용.
how: 재귀 호출 시 동일한 memo 객체를 전달해 계산된 결과를 재사용.

if n in memo:

what: n의 결과가 이미 캐시에 저장되어 있는지 확인.
why: 있으면 재계산 없이 바로 반환하여 성능을 높임.
how: dict의 키 존재 검사(평균 O(1)).

return memo[n]

what: 캐시된 값을 반환.
why: 중복 계산 배제.
how: 딕셔너리에서 값 조회 후 반환.

if n <= 1:

what: 기저 사례(0 또는 1) 처리.
why: 재귀의 종료조건이자 정확한 기본값 반환.
how: 조건문 검사.

return n

what: 기저 값 반환 (fib(0)=0, fib(1)=1).
why: 재귀 종료.
how: 반환.

memo[n] = fib(n-1, memo) + fib(n-2, memo)

what: 하위 문제들을 '재귀적'으로 계산해 더한 값을 memo에 저장.
why: 계산이 완료되면 값을 저장하여 이후 재사용.
how: 재귀 호출 시 동일 memo를 전달하여 캐시 공유.

return memo[n]

what: 계산된 값을 반환.
why: 호출자에게 결과 전달.
how: 딕셔너리 조회 반환.
'''