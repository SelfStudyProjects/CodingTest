# 3x 마을 숫자가 몇 번째인지 세는 카운터
# 3x 마을에서 사용하는 숫자 후보 (1씩 증가시킬 값)
# count가 n과 같아질 때까지 반복
# 3x 마을 숫자 후보를 1 증가
# 현재 three_x_num이 3x 마을의 규칙에 어긋나는지 확인
# 조건 1: 3의 배수인지 (three_x_num % 3 == 0)
# 조건 2: 숫자 3을 포함하는지 (str(three_x_num)에 '3'이 있는지)

# 만약 3의 배수이거나 숫자 3을 포함하고 있다면, 이 숫자는 3x 마을에서 사용할 수 없습니다.
# 따라서 count는 증가시키지 않고, 다음 three_x_num을 다시 검사해야 합니다.
# 규칙에 어긋나면 count 증가 없이 다시 while 루프의 시작으로 돌아감 (three_x_num만 증가)
# 규칙에 어긋나지 않는다면, 이 숫자는 유효한 3x 마을 숫자입니다.
# count를 1 증가시킵니다. (n번째 숫자에 한 발짝 더 가까워진 것)
# count가 n이 되었을 때의 three_x_num을 반환

def solution(n):
    count = 0
    three_x_num = 0

    while count < n:
        three_x_num += 1
        if three_x_num % 3 == 0 or '3' in str(three_x_num):
            continue
        else:
            count += 1

    return three_x_num 