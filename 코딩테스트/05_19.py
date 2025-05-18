def solution(s) :
    if s[0] == '(' and s[-1] == ')' :
        return True
    else :
        False

# 테스트 코드입니다.
print(solution('())()'))