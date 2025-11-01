# 20150111을 출력하는 함수
# 아스키 코드 기준, a는 97이고 A는 65이다.
# ord() 함수는 문자의 아스키 코드 값을 반환
# 

def print_magic_number():
    # 1. 아스키 코드를 이용해 필요한 숫자(0, 1, 2, 5)를 문자열로 생성

    # '0' 만들기: ord('a') - ord('a') 결과는 숫자 0. 이를 str()로 문자열 '0'으로 변환.
    zero = str(ord('a') - ord('a')) 
    # '1' 만들기: ord('b') - ord('a') 결과는 숫자 1. 이를 str()로 문자열 '1'으로 변환.
    one = str(ord('b') - ord('a'))
    # '2' 만들기: ord('c') - ord('a') 결과는 숫자 2. 이를 str()로 문자열 '2'로 변환.
    two = str(ord('c') - ord('a'))
    # '5' 만들기: ord('f') - ord('a') 결과는 숫자 5. 이를 str()로 문자열 '5'로 변환.
    five = str(ord('f') - ord('a'))
    
    # 2. 생성된 숫자 문자열들을 순서대로 이어 붙여 최종 문자열 생성
    result_string = two + zero + one + five + zero + one + one + one
    
    # 3. 최종 문자열 출력
    print(int(result_string))

# 함수 호출
print_magic_number()