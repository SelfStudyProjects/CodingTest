def solution(n):
    i = 1
    factorial = 1

    # 해결: while 루프와 그 안의 코드를 solution 함수 안에 **올바르게 들여쓰기**!
    while True:
        factorial *= i
        if factorial > n:
            return i - 1
        i += 1