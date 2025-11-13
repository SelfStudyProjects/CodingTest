def solution(n):
    answer = 0
    if n % 2 == 0 :
        for i in range(2, n + 2, 2) :
            answer = answer + i
    else :
        for i in range(2, n, 2) :
            answer = answer + i
    return answer