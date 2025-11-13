def solution(my_string):
    return ''.join(dict.fromkeys(my_string))

solution('people')

'''
아래 풀이도 참고!
'''

def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer+=i
    return answer