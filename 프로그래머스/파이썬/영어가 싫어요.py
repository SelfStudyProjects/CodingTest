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
= num_map을 따로 두면서 키 값에 "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" == value 값에 각각 "0", "1", "2" ... "9"를 두게끔 하는 방향성 === 어떻게 구현하는지: 파이썬 딕셔너리를 사용해 영문 숫자 단어와 그에 대응하는 숫자 문자열을 키(Key)-값(Value) 쌍으로 저장합니다. (num_map = {"zero": "0", ...})

= numbers를 입력하면 위 딕셔너리를 기준으로 키 값에 해당되는 게 있는지 확인 === 어떻게 구현하는지: current_idx를 사용해 numbers 문자열의 현재 위치를 지정하고, 파이썬 문자열 메소드인 .startswith(word, current_idx)를 활용하여 현재 위치부터 num_map의 word로 시작하는지 확인합니다.

= 키 값에 해당되는 value 값을 result_str += digit 연산을 통해 문자열로 계속 추가하며 결과값을 만들어 감 === 어떻게 구현하는지: 원본 numbers를 replace 대신, num_map에서 찾은 해당하는 digit 값을 result_str 문자열 변수에 += 연산으로 계속 추가하여 최종 결과 문자열을 구성합니다. 찾은 word의 길이만큼 current_idx를 증가시켜 이미 처리된 부분을 건너뜁니다.

= 위 과정은 while current_idx < len(numbers) 반복문을 통해서 하되, 기본적으로는 계속 반복되게끔 하기 == 계속 반복하다가 딕셔너리 기준으로 키 값이 없을 때까지 계속 반복, 없을 때는 break를 통해서 while 반복문을 중단시키는 방향성으로 가기 === 어떻게 구현하는지: while current_idx < len(numbers)를 조건으로 사용하여 numbers 문자열 전체가 처리될 때까지 반복합니다. 이 조건은 while True와 유사하게 계속 반복되지만, 모든 문자가 처리되면 자연스럽게 break 없이도 루프가 종료됩니다. 내부 for 루프에서 매칭되는 word를 찾으면 break하고, 만약 current_idx에서 어떤 word도 매칭되지 않을 경우 (found_match가 False일 경우) break를 통해 while 루프를 중단하여 네 아이디어를 반영합니다.

= 위 과정을 통해서 생긴 result_str 값들을 int(result_str)로 변환해서 최종값 == 들을 return하는 형식으로 가기 === 어떻게 구현하는지: result_str에 모든 숫자 문자열이 순서대로 저장되면, 파이썬 내장 함수 int()를 사용하여 해당 문자열을 실제 정수형으로 변환합니다. 변환된 정수 값을 return하여 최종 결과로 반환합니다.
'''

def solution(numbers):
    # 1. numbers_dictionary (num_map) 준비
    num_map = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    # 결과 숫자를 저장할 문자열
    result_str = ""

    # 'numbers' 문자열의 현재 처리 위치를 가리키는 포인터
    # (네가 while True를 통해 '계속 반복'하려는 의도를 살려봄)
    current_idx = 0 
    
    # numbers 문자열의 모든 문자를 처리할 때까지 반복
    while current_idx < len(numbers):
        # 딕셔너리의 키(영문 숫자)들을 모두 확인해봐야 해
        # 현재 위치(current_idx)부터 시작해서 어떤 영문 숫자가 매칭되는지
        found_match = False
        
        # 키들을 길이에 따라 정렬하면 더 효율적으로 탐색 가능
        # (예: 'three'가 'th'보다 먼저 매칭되도록 긴 단어 먼저 확인)
        # 하지만 이 문제에서는 'one', 'two' 같이 겹치는 접두어가 없으므로 굳이 정렬할 필요는 없음.
        
        for word, digit in num_map.items(): # 딕셔너리의 모든 (영문단어, 숫자) 쌍을 순회
            # 현재 numbers 문자열의 'current_idx' 위치부터 'word'와 일치하는지 확인
            # 예를 들어, numbers[current_idx : current_idx + len(word)]
            if numbers.startswith(word, current_idx): # Python의 startswith() 메소드를 사용하면 편리!
                result_str += digit       # 일치하면 해당 숫자를 result_str에 추가
                current_idx += len(word)  # numbers 문자열에서 해당 영문 숫자만큼 처리 위치를 이동
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