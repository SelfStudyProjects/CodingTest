def count_eights():
    answer = 0
    for number in range(1, 10001):
        answer += str(number).count('8')
    return answer

print(count_eights()) 