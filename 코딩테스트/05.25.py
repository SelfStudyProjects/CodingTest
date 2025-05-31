# DFS(깊이 우선 탐색) 구현 예시

# 1. 그래프를 인접 리스트(혹은 인접 행렬)로 표현
graph = {
    1: [2, 3, 8],
    2: [1, 7],
    3: [1, 4, 5],
    4: [3, 5],
    5: [3, 4],
    6: [7],
    7: [2, 6, 8],
    8: [1, 7]
}

# 2. 방문한 노드를 기록할 리스트(혹은 집합) 생성
visited = set()
stack = []

# 3. DFS 함수 정의
def dfs(start):
    # 시작 노드를 스택 및 방문 리스트에 추가
    stack.append(start)
    visited.append(start)
    
    start = min(graph[start])

    dfs(start)


# 4. DFS 실행(테스트코드)
dfs(1)
