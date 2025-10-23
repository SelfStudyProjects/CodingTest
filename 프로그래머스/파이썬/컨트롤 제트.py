def solution(s):
    # s를 list로 변형, 공백을 기준으로 split() 메서드 활용
    s_list = s.split() # s.split()은 기본적으로 공백 기준으로 분리

    # 최종 결과값 시작값 설정, x=0 (answer 대신 total_sum을 사용할게요!)
    total_sum = 0
    
    # Z가 나왔을 때, '바로 직전에 더했던 숫자'를 저장할 스택
    # 파이썬 리스트는 스택처럼 사용할 수 있습니다.
    num_stack = []

    # for 반복문 이용하기, s_list의 각 요소를 순회합니다.
    for item in s_list:
        # if문 활용해서, Z인지 여부에 이분법적으로 분류
        if item == "Z":
            # Z라면: num_stack에 숫자가 있을 경우에만 가장 최근에 더했던 숫자를 뺌
            if num_stack: # 스택이 비어있지 않다면
                popped_num = num_stack.pop() # 스택에서 가장 최근 숫자 제거
                total_sum -= popped_num      # 제거된 숫자를 total_sum에서 댐
        else:
            # Z가 아닐 땐: 해당 요소를 숫자로 변환하여 더함
            num = int(item)
            total_sum += num           # total_sum에 현재 숫자 더함
            num_stack.append(num)      # 이 숫자는 나중에 Z가 나올 경우를 대비해 스택에 저장

    # for 반복문 끝나면 최종값 total_sum 반환
    return total_sum