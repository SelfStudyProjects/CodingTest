# add 대신에 append 사용하기

def solution(array, height):
    sum_array = []
    for i in array :
        if i > height :
            sum_array.append(i)
    answer = len(sum_array)
    return answer

# 아래 코드도 가능

def solution(array, height):
    return sum(i > height for i in array)

"""
핵심 원리:
Python에서 불린값(True/False)은 숫자로 취급돼요:

True = 1
False = 0

단계별 분석:

i > height for i in array

각 원소가 height보다 큰지 비교해서 True/False 값들을 생성


예시로 보면:
pythonarray = [149, 180, 192, 170], height = 167

# 각 비교 결과:
149 > 167  → False (0)
180 > 167  → True  (1)  
192 > 167  → True  (1)
170 > 167  → True  (1)

# 결과: (False, True, True, True)

sum() 함수가 이것들을 더해요:
pythonsum((False, True, True, True))
= sum((0, 1, 1, 1))  
= 0 + 1 + 1 + 1 
= 3


결과:

True의 개수 = 키가 큰 사람의 수
sum()으로 True들을 모두 더하면 = 조건을 만족하는 항목의 개수
"""