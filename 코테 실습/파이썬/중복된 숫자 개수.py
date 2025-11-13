def solution(array, n):
    answer = 0
    for i in range(len(array)) :
        if array[i-1] == n :
            answer += 1
    return answer