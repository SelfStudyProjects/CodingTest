# add 대신에 append 사용하기

def solution(array, height):
    sum_array = []
    for i in array :
        if i > height :
            sum_array.append(i)
    answer = len(sum_array)
    return answer