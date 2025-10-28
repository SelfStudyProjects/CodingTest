<img width="805" height="142" alt="Image" src="https://github.com/user-attachments/assets/8dc65dba-7f8f-4e4b-b3d6-889cdb7f8eb0" />

def count_eights():
    answer = 0
    for number in range(1, 10001):
        answer += str(number).count('8')
    return answer

print(count_eights()) 