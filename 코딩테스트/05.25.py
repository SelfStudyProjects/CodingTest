# DFS 문제 풀이

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

stack = []
visited = []

# 3. DFS 함수 정의
def dfs(start):
    stack.append(start)
    visited.append(start)
    while stack:
        node = stack.pop()
        if node not in visited:



# 4. DFS 테스트 코드