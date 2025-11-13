'''
n * m  = grid
x, y = start
r, c = end
k = total steps
'''

def solution(n, m, x, y, r, c, k):
    # 모든 가능한 경로를 저장해줄 리스트
    pathlist = []

    def dfs(current_x, current_y, count, current_path_str):
        # k 걸음을 다 채웠을 경우
        if count == k:
            # r,c 도착지점에 있는지 확인
            if current_x == r-1 and current_y == c-1:
                # 도착지점에 있으면 경로를 리스트에 추가
                pathlist.append(current_path_str)
            # 도착을 못했으면 빠져나오기
            return

        # (direction_string, x, y)
        # 다운 -> x + 1
        # 업 -> x - 1
        # 왼 -> y - 1
        # 오 -> y + 1
        directions = [('d', 1, 0), ('u', -1, 0), ('l', 0, -1), ('r', 0, 1)]

        # 다음 x, y값을 업데이트
        for direction_string, nx, ny in directions:
            next_x = current_x + nx  # 다음x값 = 지금x값 + 방향값
            next_y = current_y + ny  # 다음y값 = 지금y값 + 방향값

            # 다음 x, y 값이 n*m 안에 있는지 체크
            if 0 <= next_x < n and 0 <= next_y < m:
                # 있는경우 dfs 함수 실행
                # 걸음수(count) 1 증가, 방향 문자열 추가
                dfs(next_x, next_y, count + 1, current_path_str + direction_string)

    # 출발지점 x, y, 걸음은 0, 문자열은 아무것도 없는 상태로 시작
    dfs(x-1, y-1, 0, "")


    if not pathlist:
        # 만약 pathlist안에 아무것도 없다면 k 걸음안에 도착지점에 가는게 불가능
        return "impossible"
    else:
        pathlist.sort() # alphabetical order로 정렬
        return pathlist[0] # 제일 빠른 경로를 반환

solution(3, 4, 2, 3, 3, 1, 5)