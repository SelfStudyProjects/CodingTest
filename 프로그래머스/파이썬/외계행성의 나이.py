'''
아래 포맷이 기본

def solution(age):
    answer = ''
    return answer
'''

def solution(age):
    answer = ''
    str_age = str(age)

    # 2. 문자열의 각 자리 숫자(문자)를 순회하면서 변환
    for digit_char in str_age:
        # 각 자리 숫자 문자를 실제 숫자(int)로 변환 (예: '2' -> 2)
        digit_value = int(digit_char)

        # 3. 네 아이디어! 아스키 코드 오프셋을 활용하여 숫자 -> 알파벳 변환
        # 'a'의 아스키 값에 해당 숫자 값을 더하면,
        # 0 -> 'a', 1 -> 'b', 2 -> 'c' ... 9 -> 'j' 가 됨!
        alpha_char = chr(97 + digit_value)

        answer += alpha_char # 변환된 알파벳을 answer에 추가!

    return answer
