from itertools import combinations
from collections import deque
import copy
def bfs(N, M, x, y, map_):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 상하좌우 이동방향 정보
    queue = deque([(x, y)]) # 처음 좌표를 초기값으로 설정 

    while queue: # 큐 내부에 요소가 있으면 시행
        current = queue.popleft() # 큐 제일 왼쪽 요소를 빼서 현재 좌표

        for d in directions: # (1, 0), (-1, 0), (0, 1), (0, -1)
            new_x = current[0] + d[0]
            new_y = current[1] + d[1]
            if 0 <= new_x < N and 0 <= new_y < M: # 인데스 범위를 검사
                if map_[new_x][new_y] == '0': # 0인지 확인
                    queue.append((new_x, new_y))
                    map_[new_x][new_y] = '2'
                    
N, M = map(int, input().split())
map_ = []
zero = [] # 이동가능한 공간 좌표를 저장하는 리스트
virus = [] # 바이러스들 좌표를 저장하는 리스트
max_safe = 0 # 최대값을 저장하는 변수
for i in range(N):
    line = list(input().split())
    map_.append(line) # 한 행을 map_에 삽입
    for j, num in enumerate(line): # 열거형 함수 
        if num == '0': # 0 이면 이동가능한 좌표를 저장하는 리스트에 삽입
            zero.append((i, j))
        if num == '2': # 2이면 바이러스 좌표를 저장하는 리스트에 삽입
            virus.append((i, j))

for walls in combinations(zero, 3): # 조합가능한 조합을 walls에 담아줌
    safe = 0 # 시행이 끝나고 남아있는 0의 개수
    copied_map = copy.deepcopy(map_) #[:]얕으복사 대신 깊은 복사를 사용하기 위한 모듈
    for wall in walls:
        copied_map[wall[0]][wall[1]] = '1' # 0 -> 1로 바꿔주는 코드
    for v in virus: 
        bfs(N, M, v[0], v[1], copied_map) # 모든 바이러스가 전염을 마친 상태
    for i in copied_map: # 남은 0의 개수를 새준다
        safe += i.count('0')
    max_safe = max(max_safe, safe) # 이전까지의 최대값과 현재값을 비교하여 갱신
print(max_safe) # 모든 조합, 시행에 대한 최대값