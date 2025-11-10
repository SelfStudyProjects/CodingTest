def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(10))  # 55

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

what: 하위 문제들을 재귀적으로 계산해 더한 값을 memo에 저장.
why: 계산이 완료되면 값을 저장하여 이후 재사용.
how: 재귀 호출 시 동일 memo를 전달하여 캐시 공유.

return memo[n]

what: 계산된 값을 반환.
why: 호출자에게 결과 전달.
how: 딕셔너리 조회 반환.
'''