def solution(my_string):
    my_list = list(my_string)
    answer = []
    for letter in my_list:
        answer.insert(0, letter)
    final_answer = ''.join(answer)
    return final_answer