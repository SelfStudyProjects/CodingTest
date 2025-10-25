# 다ㅅ ㄱㄱ

# 이것도 자료 구조 중에 뭐 하나 쓰는 걸로 아는데 그게 뭐지?
# 마치 스택, 큐처럼 되게 중요한 개념이었는데... 그것만 알면 잘 풀리는 문제인걸로 아는데
# 그리고 그 자료구조 속에서 board에 1이 있으면 상하좌우에서 1로 바꾸기, 이때 if문을 써서 0이면
# 1로 바꾸는 작업, 근데 여기서 5 X 5 배열 내에 있을 때만 해당 작업들을 시행하되, 그게 아니면
# 시행이 안되게끔 해야 함

def solution(board):
    n = len(board)  # board의 크기 (N x N)
    
    # 지뢰가 없는 깨끗한 지도(danger_map)를 생성하여 위험 지역을 표시할 것이다.
    # 초기에는 모든 칸이 안전(0)하다고 가정
    danger_map = [[0] * n for _ in range(n)]

    # 주변 8칸 (대각선 포함)과 자기 자신을 표시하기 위한 방향 벡터
    # (dr, dc) = (delta row, delta column)
    #               상       하       좌       우    좌상단   우상단   좌하단   우하단
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1), (0, 0)]
    # (0, 0)은 지뢰 자신을 표시하기 위함

    # 원본 board를 순회하며 지뢰(1)를 찾는다.
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:  # 지뢰를 발견했다면
                # 해당 지뢰 주변 8칸과 자신을 danger_map에 위험(1)으로 표시
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc  # 새로운 행(nr), 새로운 열(nc) 좌표 계산

                    # # 5 X 5 배열 내에 있을 때만 해당 작업들을 시행 (경계 조건 체크)
                    # 계산된 새로운 좌표가 board의 유효한 범위 내에 있는지 확인
                    if 0 <= nr < n and 0 <= nc < n:
                        danger_map[nr][nc] = 1 # danger_map에 위험 지역으로 표시

    # 안전한 지역의 칸 수를 계산 (danger_map에서 0인 칸의 개수)
    safe_area_count = 0
    for r in range(n):
        for c in range(n):
            if danger_map[r][c] == 0:  # danger_map에서 0은 안전 지역을 의미
                safe_area_count += 1

    return safe_area_count