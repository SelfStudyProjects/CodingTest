# 소요 시간 : 40분 
# 정오답 여부 : 오
# 구현해야 하는 기능 및 구현 방법 : 반으로 접는 것(if문, /=), 홀수일 때 버리는 것(if, trunc)
# 구현해야 하는 기능 및 구현 방법 : 회전 후 지갑에 넣는 것(for문), max 함수끼리 비교(지폐-지갑), min 함수끼리 비교(지폐-지갑)
# 사용할 변수들 : wallet 리스트, bill 리스트, solution 함수, answer 변수
# 1단계, 접은 횟수를 저장할 변수 설정 : answer = 0
# 2단계, 지폐 크기가 지갑 크기에 들어갈 때까지 반복 : while 반복문
# 3단계, 지폐 크기가 지갑 크기에 들어갈 때까지 반복 : while 반복문
# 4단계, 지폐의 가로가 세로보다 크는 경우 : if, //=
# 5단계, 지폐의 가로가 세로보다 크지 않은 경우 : else, //=
# 6단계. answer 1 증가 : += 1



def solution(wallet, bill):
    answer = 0
    
    while (min(bill) > min(wallet)) or (max(bill) > max(wallet)):
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
            
        answer += 1
    
    return answer