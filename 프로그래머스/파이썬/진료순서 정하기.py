''' 
첫번째, sorted를 해서 리스트업(내림차순)을 하기
두번째, for 반복문을 활용, 리스트업된 리스트(=리스트업)의 기준으로 순차적으로 값을 도출하고
세번째, emergency를 딕셔너리로 변용 후 활용해서, 값을 기준으로 mapping을 한다.
네번째, emergency의 값을 각각 리스트업의 '인덱스 + 1' 값들로 변환, 이때는 replace 함수 활용
'''

def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True) # 원래 기본이 내림차순
    answer = []
    
    for e in emergency:
        rank = sorted_emergency.index(e) + 1  # 인덱스는 0부터 시작하므로 +1
        answer.append(rank)
        
    return answer