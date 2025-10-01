def solution(before, after):
    # 두 문자열을 각각 정렬해서 비교.
    # 애너그램이라면 정렬했을 때 완전히 같은 문자열이 됨.
    if sorted(before) == sorted(after):
        return 1
    else:
        return 0
    
    # 한 줄로도 가능: return 1 if sorted(before) == sorted(after) else 0

'''
아래 내용도 괜찮음 참고해보기
'''

def solution(before, after):
    
    after_list = list(after) 
    
    for char_b in before:
        if char_b in after_list:
            after_list.remove(char_b)
        else:
            return 0
            
    # 아무것도 없을 때 false, 있다면 true
    if not after_list: # after_list가 비어있으면 True
        return 1
    else: # after_list가 비어있지 않으면 False
        return 0
