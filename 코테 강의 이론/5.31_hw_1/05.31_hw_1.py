def solution(n, m, x, y, r, c, k):
    
    answer = '' # 루트 경로 답을 담을 곳
    final_answer = "impossible" # 오답일 때 리턴값 
    found_it = False

    initial_min_dist = abs(x - r) + abs(y - c)

    if initial_min_dist > k or (k - initial_min_dist) % 2 != 0:
        return final_answer

    dx = [1, 0, 0, -1] # 각 방향으로 이동했을 때 x좌표(세로) 변화량
    dy = [0, -1, 1, 0] # 각 방향으로 이동했을 때 y좌표(가로) 변화량
    dirs = ['d', 'l', 'r', 'u'] # 각 방향을 나타내는 문자

    def solve(cur_x, cur_y, path, dist):
        nonlocal final_answer, found_it

        if found_it:
            return

        min_dist_to_target = abs(cur_x - r) + abs(cur_y - c)
        remaining_k = k - dist

        if min_dist_to_target > remaining_k:
             return # 이 경로는 가망 없어! 바로 탐색 중단!

        if dist == k:
            if cur_x == r and cur_y == c:
                found_it = True 
            return 

        for i in range(4): # 네 방향 (아래, 왼쪽, 오른쪽, 위) 모두 시도
            next_x = cur_x + dx[i] # i번째 방향으로 이동했을 때의 다음 x 좌표 계산
            next_y = cur_y + dy[i] # i번째 방향으로 이동했을 때의 다음 y 좌표 계산

            # (미로 바깥으로는 나갈 수 없으니까!)
            if 1 <= next_x <= n and 1 <= next_y <= m:
                solve(next_x, next_y, path + dirs[i], dist + 1)

    solve(x, y, "", 0)

    answer = final_answer

    return answer
