def solution(order):
    character = str(order)
    answer = 0
    for i in character :
        if i in ['3', '6', '9'] :
            answer += 1
    return answer