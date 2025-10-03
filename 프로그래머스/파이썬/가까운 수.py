def solution(array, n):
    return sorted(array, key=lambda x: abs(x - n))[0]

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