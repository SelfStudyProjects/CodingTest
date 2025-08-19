import numpy as np

def solution(numbers):
    answer = np.sum(numbers) / len(numbers)
    return answer

# 위의 것도 오키, 그리고 아래 것도 오키

def solution(numbers):
    answer = 0
    sum = 0
    for i in numbers :
        sum += i
    answer = sum / len(numbers)
    return answer