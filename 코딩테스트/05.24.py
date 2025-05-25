import math

def solution(N, A, B):
    21 <= N <= 220, A <= N, B <= N, A != B
    # 2개씩 묶어주기
    # 그리고 2로 나누어주기
    # 위 과정 반복(for , while, 재귀 함수)
    # 2의 지수... (３２, ６４, １２８)
    # 1, 2 / 3, 4, / 5, 6 / 7, 8
    # 2씩 나눌 때, 짝수는 그대로 홀수는 1을 더해주기
    # 2개 숫자 중 홀수에 1을 더할 때 짝수 쪽 숫자가 되면 종료
    i = 0
    for i in range(int(math.log2(N))): # 2의 지수 만큼 반복
        A = (A + 1) // 2
        B = (B + 1) // 2
        if A != B:
            i += 1
        else:
            return i

# 테스트 코드입니다.
print(solution(8, 4, 7))