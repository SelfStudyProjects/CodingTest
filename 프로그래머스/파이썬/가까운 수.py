def solution(array, n):
    return sorted(array, key=lambda x: (abs(x - n), x))[0]

# 차익을 절댓값 씌운 후, 내림차순 배열. 그리고 가장 큰값을 인덱스 0을 두어서 추출하는 로직

'''
정렬 기준 지정 (key 매개변수)
key 매개변수에 함수를 지정하면, 해당 함수의 실행 결과를 기준으로 정렬할 수 있습니다. 
튜플 리스트 정렬: 각 튜플의 두 번째 요소를 기준으로 정렬합니다.

tuples = [(1, 'B'), (3, 'A'), (2, 'C')]
sorted_by_second = sorted(tuples, key=lambda x: x[1])
print(sorted_by_second)  # 출력: [(3, 'A'), (1, 'B'), (2, 'C')]
'''

'''
add = lambda x, y: x + y
print(add(5, 3)) # 출력: 8
'''

# sorted 함수 기준, True 내림차순-False 오름차순
# 가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다. 이 지점에 초점!
# [3, 10, 28, 30, 12] => [17, 10, 8, 10, 8]
# [3, 10, 28, 30, 12] => [(17, 3), (10, 10), (8, 28), (10, 30), (8, 12)]
# 원하는 숫자: 20
# result: 28

# array = [3, 10, 28, 30, 12]
# n = 20

# 28 - 20 == 8
# 12 - 20 == -8

# 20 - 28 == -8
# 20 - 12 == 8

# sorted(array, key=lambda x:(abs(x-n), x))[0]
# sorted(array, key=lambda x:(abs(x-n), n-x))[0] # 팁, n-x이거나 x-n 2개 중에 하나입니다.