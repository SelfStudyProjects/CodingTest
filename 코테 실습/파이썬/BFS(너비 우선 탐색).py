'''
문제 설명
인접 리스트로 표현된 그래프와 시작 정점 start가 주어질 때, 너비 우선 탐색(BFS)을 사용하여
시작점으로부터의 방문 순서를 출력하거나 리스트 형태로 반환하세요. 방문한 정점은 다시 방문하지 않도록 처리해야 합니다.
BFS는 큐(선입선출)를 사용해 먼저 들어간(탐색 후보로 등록된) 노드를 먼저 처리합니다.
'''
from collections import deque

def bfs(graph, start):
    visited = set()
    order = []             # 방문 순서를 저장할 리스트
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

# 예시 사용
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}
print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E']