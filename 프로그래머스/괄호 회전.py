# 기존 포맷
# def solution(s):
#     answer = -1
#     return answer

def solution(s):
    answer = -1 # 왜 0이 아니라 -1일까?
    answer += 1
    stack = []
    num = len(s) # 원소의 총 개수 세기
    for i in range(num) : # for 반복문(num 수만큼 반복하기)
        answer += 1
        t = s[i:] + s[:i-1]

    # (), {}, [] 종류 구분하기
    # 아래 메커니즘에 따라서 각 종류마다 모두 해당되는 경우가 있는지 체킹

    for char in s:
        if char in ['[', '(', '{']:
            stack.append(char)
        elif char in [']', ')', '}']:
            if stack:
                stack.pop()
            else:
                return False

    return len(stack) == 0
    return answer