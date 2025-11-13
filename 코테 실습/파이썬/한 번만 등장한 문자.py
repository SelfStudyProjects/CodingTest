from collections import Counter

def solution(s):
    char_counts = Counter(s)
    unique_chars_list = []
    
    for i in s:
        if char_counts[i] == 1:
            if i not in unique_chars_list:
                unique_chars_list.append(i)
    unique_chars_list.sort() 

    return "".join(unique_chars_list)

    #    정렬된 문자들을 하나의 문자열로 합쳐서 반환!
    #    만약 unique_chars_list가 비어있으면, ''.join([])는 빈 문자열 ''을 반환하므로 문제의 조건에 맞음.
    #    정렬된 문자들을 하나의 문자열로 합쳐서 반환!
    #    만약 unique_chars_list가 비어있으면, ''.join([])는 빈 문자열 ''을 반환하므로 문제의 조건에 맞음.

    
# Counter() 메소드를 안써도 되어서 훨씬 심플
def solution(s):
    answer = ''
    list_s = list(s)
    list_s.sort()
    for i in list_s:
        if list_s.count(i)==1:
            answer+=i
    return answer