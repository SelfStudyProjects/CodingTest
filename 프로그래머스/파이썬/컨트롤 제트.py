# s를 list로 변형, 공백을 기준으로 split() 메서드 활용
# s.split()은 기본적으로 공백 기준으로 분리
# 최종 결과값 시작값 설정, x=0 (answer 대신 total_sum을 사용할게요!)
# Z가 나왔을 때, '바로 직전에 더했던 숫자'를 저장할 스택
# 파이썬 리스트는 스택처럼 사용할 수 있습니다.
# for 반복문 이용하기, s_list의 각 요소를 순회합니다.
# if문 활용해서, Z인지 여부에 이분법적으로 분류
# Z라면: num_stack에 숫자가 있을 경우에만 가장 최근에 더했던 숫자를 뺌
# 스택이 비어있지 않다면
# 스택에서 가장 최근 숫자 제거
# 제거된 숫자를 total_sum에서 댐
# Z가 아닐 땐: 해당 요소를 숫자로 변환하여 더함
# total_sum에 현재 숫자 더함
# 이 숫자는 나중에 Z가 나올 경우를 대비해 스택에 저장
# for 반복문 끝나면 최종값 total_sum 반환

'''
스택은 데이터를 일시적으로 저장하는 선형 자료구조로, LIFO(Last-In, First-Out) 원칙에 따라
가장 나중에 삽입된 데이터가 가장 먼저 인출됩니다. 주요 연산으로는 데이터를 삽입하는 푸시(Push)와 가장 위에 있는 데이터를
제거하며 반환하는 팝(Pop)이 있습니다. 일반적으로 함수 호출 관리, 웹 브라우저 방문 기록 등 가장 최근에 발생한 작업을 처리할 때 활용됩니다.
'''

def solution(s):
    s_list = s.split()

    total_sum = 0
    num_stack = []

    for item in s_list:
        if item == "Z":
            if num_stack:
                popped_num = num_stack.pop()
                total_sum -= popped_num
        else:
            num = int(item)
            total_sum += num           
            num_stack.append(num) 

    return total_sum