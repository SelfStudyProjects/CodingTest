def solution(my_string):
    # 1. 문자열을 문자 단위 리스트로 변환 (처리 용이)
    #    예: "hello" -> ['h', 'e', 'l', 'l', 'o']
    my_list = list(my_string)
    
    # 뒤집힌 문자를 저장할 빈 리스트
    answer = []
    
    # 2. 리스트 순회하며 각 문자를 'answer' 리스트 맨 앞에 삽입 (insert(0, ...))
    #    -> 결과적으로 문자들이 역순으로 쌓여 뒤집힌 리스트 생성
    #    예: 'j' -> ['j'] / 'a' -> ['a', 'j'] / ... / 'n' -> ['n', 'o', 'r', 'a', 'j']
    for letter in my_list:
        answer.insert(0, letter)
        
    # 3. 뒤집힌 문자 리스트를 하나의 문자열로 합치기 (''.join(...))
    #    -> 리스트 요소들을 연결하여 최종 문자열 반환
    final_answer = ''.join(answer)
    
    return final_answer
