# 2
from itertools import combinations
from copy import deepcopy
from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(graph,start,n,m):
    queue = deque([start])
    # 바이러스 시작 위치가 start이기에 start에서의 값은 2
    # 그 주변에 0이 있으면 0을 2로 바꾸면 됨

    while queue:
        x, y = queue.popleft()
        for i in range(4): # 이동할 수 있는 방향이 4개 이기에
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 이동한 방향이 인덱스를 넘지 않았고
            # 이동한 곳의 값이 0이면 바이러스가 확산될 것이니 2로 바꾸고
            # 그 위치에서 다시 바이러스를 확산(queue에 넣어서 이 다음에 확산) 시키는 코드
            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx,ny))


def virus_go(graph,virus,n,m):
    # 바이러스 위치들을 알고 있으니
    # 각 바이러스 위치에서 bfs를 통해 바이러스를 확산시킴
    for i, j in virus:
        bfs(graph,(i,j),n,m)
    
    # 남은 안전 지역의 수 확인
    sum = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                sum += 1
    return sum


def solution(graph,n,m):
    avail = []
    virus = []
    answer = 0

    # 벽을 세우려면 어디를 세울 수 있는지 부터 확인해야 하기에
    # 전체를 다 돌기는 해야하는데, 어짜피 전체를 돌 것이기에
    # 돌면서 virus 위치도 같이 세어주는게 좋음
    # 0은 벽을 새로 새울 수 있음, 2는 바이러스가 퍼짐 이라는
    # 특이한 로직이 가능한 애들이고 1은 그러지는 않아서
    # 이미 세워진 벽인 1은 굳이 안 모아줘도 괜찮음
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                avail.append((i,j))
            elif graph[i][j] == 2:
                virus.append((i,j))

    # 생각보다 많이 사용하는 함수, combinations(리스트,갯수)
    # 리스트에서 순서 고려하지 않고 갯수 만큼 뽑아내는
    # 모든 경우의 수를 리턴해 주는 함수
    for wall in combinations(avail,3):
        new_graph = deepcopy(graph)
        # 그래프를 줘야 하는데 벽이 새로 세워진 그래프가 들어가야 하는데
        # 매번 세워지는 벽에 따라 그래프가 달라지고 (원본을 기억해야 하고)
        # 원본으로 다시 되돌리는 (=백트래킹)을 해도 되지만
        # 벽 3개를 되돌리는 것 보다 원본을 기억하는게 낫다고 판단
        # 2차원 리스트기에 graph[:] 로 복사했다가는 내부 리스트는 그대로 복사됨 (얕은 복사)
        # 즉, graph[:]를 사용하면 사실상 원래 그래프 조차도 변형됨 -> 깊은 복사를 해야함
        for i,j in wall:
            new_graph[i][j] = 1
        result = virus_go(new_graph,virus,n,m)
        
        # 결과로 나온 안전 지역의 수가 이전까지의 안전 지역의 수 보다 많으면
        # 그 결과로 기억하고 있어라
        if result > answer:
            answer = result
    return answer

if __name__ == "__main__":
    print(solution(graph,n,m))