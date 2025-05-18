def solution(s):
    stack = []
    ran # 원소의 총 개수 세기
    # 인덱스 0 pop, 인덱스 -1 add 함수
    # (), {}, [] 종류 구분하기
    # 아래 메커니즘에 따라서 각 종류마다 모두 해당되는 경우가 있는지 체킹
    def solution(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return False
    
    return len(stack) == 0

    answer = -1 # 왜 0이 아니라 -1일까?
    return answer