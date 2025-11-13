'''
에러가 난 곳은 바로 이 줄이야: if i in list['3', '6', '9'] :

list의 의미: 파이썬에서 list라고 그냥 쓰면, 이건 우리가 알고 있는 [ ]로 만드는 '리스트' 자체가 아니라, list라는 데이터 타입 그 자체를 의미해. 마치 int, str 같은 것들처럼 말이지!

[]의 역할: 네가 list['3', '6', '9']처럼 [] (대괄호)를 사용했는데, []는 주로 **실제 리스트(객체)**에서 인덱싱(my_list[0])을 하거나 슬라이싱(my_list[1:3])을 할 때 사용하는 문법이야.

에러 발생 지점: 그래서 파이썬 인터프리터가 list라는 '타입(type)'에 대고 인덱싱/슬라이싱을 하려고 하니 "아니, list는 타입이지, 인덱싱이나 슬라이싱 할 수 있는 객체가 아니야!" 라고 말하면서 TypeError: 'type' object is not subscriptable 에러를 낸 거야! (subscriptable은 '인덱싱/슬라이싱 할 수 있는' 이라는 뜻!)
'''

def solution(order):
    character = str(order)
    answer = 0
    for i in character :
        if i in ['3', '6', '9'] :
            answer += 1
    return answer