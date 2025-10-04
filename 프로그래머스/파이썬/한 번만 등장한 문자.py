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