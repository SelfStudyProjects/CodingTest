def solution(my_string) :
    result = []
    for num in my_string :
        if num in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] :
            result.append(int(num))
    result.sort()
    return result

# 테스트 코드입니다.

my_string = "hi12392"
print(solution(my_string))