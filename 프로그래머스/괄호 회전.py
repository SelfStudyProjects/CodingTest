# 기존 포맷
# def solution(s):
#     answer = -1
#     return answer

def solution(s):
    answer = -1
    answer += 1
    num = len(s) # 문자열 길이
    
    # 괄호 짝을 딕셔너리로 정의!
    bracket_pairs = {'[': ']', '(': ')', '{': '}'}

    # 문자열을 num번 회전시키는 반복문 시작!
    for i in range(num):
        stack = [] # 스택 초기화! (매 회전마다 스택은 비어있어야 함!)
        rotated_s = s[i:] + s[:i] # i번째 회전된 문자열 만들기!
        
        # rotated_s의 각 문자에 대해 괄호 체크!
        for char in rotated_s:
            if char in ['[', '(', '{']: # 여는 괄호면 스택에 push!
                stack.append(char)
            elif char in [']', ')', '}']: # 닫는 괄호면?
                if stack: # 스택이 비어있지 않으면?
                    top = stack.pop() # 스택의 가장 위
                    if bracket_pairs[top] != char :
                        stack = None
                        break
                else:
                    stack = None
                    break
        if stack == [] :
            answer += 1
    return answer