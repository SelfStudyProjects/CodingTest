# 3
from collections import deque
N, K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
S, X, Y = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(graph,N,K,S,X,Y):
    virus = []  # 바이러스 위치들을 모아놓을 리스트

    for i in range(N):
        for j in range(N):
            node = graph[i][j]
            if node != 0:  # 0이면 바이러스가 없다는 것이기에
                virus.append((node,(i,j),0))  # 바이러스의 값, 위치, 이동 시간(S초 확인 때문에)
    
    # 바이러스 값이 작은 것 부터 순서대로 하기에 들어온 순서대로 하는 queue를 사용
    virus.sort(key=lambda x : x[0])  # 바이러스의 값이 작은 것 부터 확산을 시키기에 정렬
    queue = deque(virus) # 바이러스 값이 적은 것 부터 queue에 들어있게 됨

    while queue:
        node, (x, y), time = queue.popleft()

        if time >= S:  # S초 까지만 확인하면 되기에
            # 이걸 위해서 virus 리스트랑 queue에 시간까지 넣은 것이고
            # bfs기에 0초 부터 순서대로 쌓여가서 S초가 한 번 이라도 나오는 순간 끝내면 됨
            # dfs면 초가 순서대로 안 나오기에 확인 로직이 어려울 수 있음
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N and graph[nx][ny] == 0:
                graph[nx][ny] = node
                queue.append((node,(nx,ny),time+1))
    return graph[X][Y]

if __name__ == "__main__":
    print(solution(graph,N,K,S,X-1,Y-1))