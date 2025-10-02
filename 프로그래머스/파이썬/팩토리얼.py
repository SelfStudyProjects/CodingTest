def solution(n):
    i = 1
    factorial = 1

    while True:
        factorial *= i
        if factorial > n:
            return i - 1
        i += 1