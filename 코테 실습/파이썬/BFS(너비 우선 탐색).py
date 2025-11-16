'''
* 문제 설명
인접 리스트로 표현된 그래프와 시작 정점 start가 주어질 때, 너비 우선 탐색(BFS)을 사용하여
시작점으로부터의 방문 순서를 출력하거나 리스트 형태로 반환하세요. 방문한 정점은 다시 방문하지 않도록 처리해야 합니다.
BFS는 큐(선입선출)를 사용해 먼저 들어간(탐색 후보로 등록된) 노드를 먼저 처리합니다.

* 알고리즘/자료구조 구체적 설명 — BFS와 큐

정의: 너비 우선 탐색(BFS)은 한 정점에서 시작하여 같은 거리(레벨)에 있는 모든 정점을 먼저 방문한 뒤,
그 다음 레벨로 넘어가는 탐색 방법.

핵심 자료구조: 큐(선입선출, FIFO) — 먼저 발견된 노드를 먼저 처리하여 레벨 단위 탐색 보장.
시간복잡도: O(V + E) — 각 정점과 간선은 한 번씩만 처리됨(인접 리스트 기준). V는 정점 수, E는 간선 수.
공간복잡도: O(V) — visited 집합과 큐에 최대 V개 항목이 들어갈 수 있음.
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