# 써야 하는 함수 :
# 정의내려야 하는 것들(def) : time_to_seconds, seconds_to_time, solution
# 구현해야 하는 기능들 : commands 한개씩 분할(for in), prev(-=, if문 10초 미만), next(+=, if문 video_len 초과), if문 활용(op_start ≤ 현재 재생 위치 ≤ op_end -> op_end)


def time_to_seconds(time):
    minutes, seconds = map(int, time.split(':'))
    return minutes * 60 + seconds

def seconds_to_time(total_seconds):
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes:02}:{seconds:02}"

def solution(video_len, pos, op_start, op_end, commands):
    video_length = time_to_seconds(video_len)
    current_pos = time_to_seconds(pos)
    opening_start = time_to_seconds(op_start)
    opening_end = time_to_seconds(op_end)

    for command in commands:
        
        if opening_start <= current_pos <= opening_end:
            current_pos = opening_end
        
        if command == "prev":
            current_pos -= 10
            if current_pos < 0:
                current_pos = 0
                
        elif command == "next":
            current_pos += 10
            if current_pos > video_length:
                current_pos = video_length
        
    if opening_start <= current_pos <= opening_end:
        current_pos = opening_end

    answer = seconds_to_time(current_pos)
    return answer

# 테스트용 코드
print(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"]))  # "13:00"
print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]))  # "06:55"
print(solution("07:22", "04:05", "00:15", "04:07", ["next"]))  # "04:17"