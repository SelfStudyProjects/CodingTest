# 다시 풀기

# 1. 결과를 저장할 빈 리스트를 준비합니다.
#    문자열은 불변(immutable)이라, '+' 연산으로 문자열을 계속 합치면 비효율적일 수 있습니다.
#    리스트에 조각들을 저장 후 마지막에 join()으로 합치는 것이 더 효율적입니다.
# 2. 입력 문자열이 비어있는 경우 처리 (예외 방지)
# 3. 첫 번째 문자를 previous_char에 저장하고, count를 1로 초기화합니다.
#    (문자열의 첫 문자는 항상 새로운 묶음의 시작이므로, count=1로 시작)
# 4. 두 번째 문자부터 마지막 문자까지 for 반복문을 돌면서 순회합니다.
# range(1, len(s))는 인덱스 1부터 문자열의 끝까지를 의미합니다.
# 현재 문자가 이전 문자와 같다면, 연속되는 횟수를 증가시킵니다.
# 현재 문자가 이전 문자와 다르다면, 이전 문자의 압축 결과를 추가하고 상태를 갱신합니다.
# 이전 문자의 압축 결과 (문자 + 횟수)를 결과 리스트에 추가합니다.
# 예: 'a' + '3' -> 'a3'
# 새로운 묶음의 시작이므로, previous_char를 현재 문자로 업데이트하고 count를 1로 초기화합니다.
# 5. 반복문이 끝난 후, 마지막으로 남아있는 previous_char와 count를 result에 추가합니다.
#    반복문은 문자열 끝까지 돌지만, 마지막 묶음은 'else' 블록을 만나지 못하므로 따로 처리해야 합니다.
# 6. 결과 리스트의 모든 요소를 하나의 문자열로 합쳐서 반환합니다.
#    ['a', '3', 'b', '2', 'c', '6', 'a', '1'] -> "a3b2c6a1"

'''
[문제]

문자열을 입력받아서, 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시하여 문자열을 압축하기.
입력 예시: aaabbcccccca
출력 예시: a3b2c6a1
'''

def solution(s):
    compressed_parts = [] # 배열(리스트) 선언
    if not s:
        return ""

    previous_char = s[0]
    count = 1

    for i in range(1, len(s)):
        current_char = s[i] # 현재 순회 중인 문자

        if current_char == previous_char: # 이전 문자와 같다면
            count += 1
        else: # 이전 문자와 다르다면
            compressed_parts.append(previous_char)
            compressed_parts.append(str(count)) # count는 숫자이므로 문자열로 변환하여 추가

            previous_char = current_char # 이전 문자를 현재 문자로 갱신
            count = 1 # 새로운 문자이므로 count를 1로 초기화
    
    compressed_parts.append(previous_char) # 마지막 문자 처리
    compressed_parts.append(str(count))

    return "".join(compressed_parts) # 배열의 요소들을 하나의 문자열로 합쳐서 반환

# 입출력 예시 확인
print(solution("aaabbcccccca"))  # 출력: a3b2c6a1
print(solution("aabb"))        # 출력: a2b2
print(solution("abc"))         # 출력: a1b1c1
print(solution("aaaaa"))        # 출력: a5
print(solution(""))            # 출력: ""
print(solution("a"))           # 출력: a1