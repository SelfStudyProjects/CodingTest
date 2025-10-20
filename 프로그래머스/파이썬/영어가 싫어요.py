# 다시 풀기 

# numbers_dictionary를 따로 두면서 키 값에 "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
## value 값에 각각 0, 1, 2 ... 9를 두게끔 하는 방향성
# numbers를 입력하면 위 딕션너리를 기준으로 키 값에 해당되는 게 있는지 확인
# 키 값에 해당되는 value 값을 바꾸는 메소드 쓰기
# 위 과정은 while 반복문을 통해서 하되, 기본적으로는 게속 반복되게끔 하기 While(True)문과 같은 형식을 써서
## 계속 반복하다가 딕션너리 기준으로 키 값이 없을 때까지 계속 반복, 없을 때는 return 0을
### 통해서 while 반복문을 중단시키는 방향성으로 가기
# 위 과정을 통해서 생긴 value 값들을 add 메소드로 해서 문자열로 계속 추가해서 해당 최종값
## 들을 return하는 형식으로 가기

'''
= num_map을 따로 두면서 키 값에 "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" == value 값에
각각 "0", "1", "2" ... "9"를 두게끔 하는 방향성 === 어떻게 구현하는지:
파이썬 딕셔너리를 사용해 영문 숫자 단어와 그에 대응하는 숫자 문자열을 키(Key)-값(Value) 쌍으로 저장합니다.
(num_map = {"zero": "0", ...})

= numbers를 입력하면 위 딕셔너리를 기준으로 키 값에 해당되는 게 있는지 확인 === 어떻게 구현하는지:
current_idx를 사용해 numbers 문자열의 현재 위치를 지정하고, 파이썬 문자열 메소드인 .startswith(word, current_idx)를 활용하여
현재 위치부터 num_map의 word로 시작하는지 확인합니다.

= 키 값에 해당되는 value 값을 result_str += digit 연산을 통해 문자열로 계속 추가하며 결과값을 만들어 감 === 어떻게 구현하는지:
원본 numbers를 replace 대신, num_map에서 찾은 해당하는 digit 값을 result_str 문자열 변수에 += 연산으로 계속 추가하여 최종 결과
문자열을 구성합니다. 찾은 word의 길이만큼 current_idx를 증가시켜 이미 처리된 부분을 건너뜁니다.

= 위 과정은 while current_idx < len(numbers) 반복문을 통해서 하되, 기본적으로는 계속 반복되게끔 하기 ==
계속 반복하다가 딕셔너리 키 값이 없을 때까지 계속 반복, 없을 때는 break를 통해서 while 반복문을 중단시키는
방향성으로 가기 === 어떻게 구현하는지: while current_idx < len(numbers)를 조건으로 사용하여 numbers 문자열 전체가 처리될 때까지
반복합니다. 이 조건은 while True와 유사하게 계속 반복되지만, 모든 문자가 처리되면 자연스럽게 break 없이도 루프가 종료됩니다.
내부 for 루프에서 매칭되는 word를 찾으면 break하고, 만약 current_idx에서 어떤 word도 매칭되지 않을 경우 (found_match가 False일 경우)
break를 통해 while 루프를 중단하여 네 아이디어를 반영합니다.

= 위 과정을 통해서 생긴 result_str 값들을 int(result_str)로 변환해서 최종값 ==
들을 return하는 형식으로 가기 === 어떻게 구현하는지: result_str에 모든 숫자 문자열이 순서대로 저장되면,
파이썬 내장 함수 int()를 사용하여 해당 문자열을 실제 정수형으로 변환합니다. 변환된 정수 값을 return하여 최종 결과로 반환합니다.
'''

def solution(numbers):
    num_map = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    result_str = ""
    current_idx = 0 
    
    while current_idx < len(numbers):
        found_match = False
        
        
        for word, digit in num_map.items():
            # 딕셔너리의 모든 요소들의 각 값 및 인덱스에 대해 for 반복문 시행
            # 두 문자열 비교: startswith(prefix_string, start_index)는 self 문자열(여기서는 numbers 문자열)의 start_index 위치부터
            # prefix_string (여기서는 word)과 정확히 일치하는지 비교해.
            if numbers.startswith(word, current_idx):
                # Python의 startswith() 메소드를 사용하면 편리!
                # 근데 startswitch() 메소드는 어떻게 구현되고? 왜 여기서 사용되었을까?
                result_str += digit       # 일치하면 해당 숫자를 result_str에 추가
                current_idx += len(word)
                # numbers 문자열에서 해당 영문 숫자만큼 처리 위치를 이동
                found_match = True        # 매칭되는 단어를 찾았음을 표시
                break                     # 현재 위치에서 하나의 영문 숫자를 찾았으니 다음 위치로 이동
        
        # 만약 current_idx 위치에서 어떤 영문 숫자도 찾지 못했다면 (이 문제는 이런 상황이 발생하지 않겠지만, 일반적인 패턴)
        if not found_match:
            # 예상치 못한 상황 (문제 조건에는 없음) 또는 while 루프를 중단시켜야 할 경우
            # 이 문제의 경우 모든 숫자가 영문으로 변환될 수 있으므로 이 블록에 도달할 일은 없을 거야.
            # 하지만 네 의도("없을 때는 반복 중단")를 살리면 이런 로직이 들어갈 수 있어.
            break 
            
    # 최종 결과 문자열을 정수로 변환하여 반환
    return int(result_str)