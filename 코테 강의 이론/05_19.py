# def solution(s) :
#     if s[0] == '(' and s[-1] == ')' :
#         return True
#     else :
#         False

# # 테스트 코드입니다.
# print(solution('())()'))

# # 교수님 코드입니다

# def solution(s) :
#     stack = []
#     for i in s :
#         if i == "(":
#             stack.append(i)
#         elif i == ")"

def solution(s):
    stack = []  # 괄호를 저장할 스택 초기화
    
    for char in s:  # 문자열의 각 문자에 대해 반복
        if char == '(':  # 여는 괄호일 경우
            stack.append(char)  # 스택에 추가
        elif char == ')':  # 닫는 괄호일 경우
            if stack:  # 스택이 비어있지 않으면
                stack.pop()  # 스택에서 여는 괄호 제거
            else:
                return False  # 여는 괄호가 없으므로 false 반환
    
    return len(stack) == 0  # 스택이 비어있으면 true, 아니면 false

# 예시 테스트
print(solution("()"))        # 출력: True
print(solution("(()())"))    # 출력: True
print(solution(")("))        # 출력: False
print(solution("((())"))     # 출력: False
print(solution("(())))"))    # 출력: False