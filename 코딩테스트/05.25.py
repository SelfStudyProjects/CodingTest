# DFS(깊이 우선 탐색) 구현 예시

# 1. 그래프를 인접 리스트(혹은 인접 행렬)로 표현
graph = {
    1: [2, 3],
    2: [1, 7],
    3: [1, 4, 5],
    4: [3, 6],
    5: [3, 6],
    6: [4, 5, 7],
    7: [2, 6]
}

# 2. 방문한 노드를 기록할 리스트(혹은 집합) 생성
visited = set()

# 3. DFS 함수 정의
def dfs(start):
    # 3-1. 스택을 이용해 구현 (재귀로도 가능)
    stack = []
    # 3-2. 시작 노드를 스택에 추가
    stack.append(start)
    
    # 3-3. 스택이 빌 때까지 반복
    while stack:
        # 3-4. 스택에서 노드를 꺼내 방문 처리
        node = stack.pop()
        if node not in visited:
            # 3-5. 방문한 노드 기록
            visited.add(node)
            print(node, end=' ')  # 방문 순서 출력(옵션)
            
            # 3-6. 인접 노드 중 방문하지 않은 노드를 스택에 추가
            # (이미지처럼 가장 마지막에 추가된 노드부터 방문)
            # 구현 시, 인접 노드를 역순으로 추가하면 이미지와 동일한 순서로 탐색 가능
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# 4. DFS 실행
dfs(1)
