'''
* 문제 설명
인접 리스트로 표현된 그래프와 시작 정점 start가 주어질 때, 너비 우선 탐색(BFS)을 사용하여
시작점으로부터의 방문 순서를 출력하거나 리스트 형태로 반환하세요. 방문한 정점은 다시 방문하지 않도록 처리해야 합니다.
BFS는 큐(선입선출)를 사용해 먼저 들어간(탐색 후보로 등록된) 노드를 먼저 처리합니다.

* 기호 설
튜플(tuple): ( ) (소괄호)
딕셔너리(dictionary): {} (중괄호, 키:값 쌍)
리스트(list): [ ] (대괄호)

None으로 두고 함수 내부에서 생성하는 이유
visited=None으로 기본값을 주면,
최초 호출에서만 set()을 새로 만들고,
이후 재귀 호출에선 이미 만들어진 집합을 계속 전달함.

순서가 중요하면 리스트 사용
리스트: 순서 O, 중복 O, 변경 O, 대괄호[] 사용, 인덱스 접근
튜플: 순서 O, 중복 O, 변경 X, 소괄호() 사용, 불변 데이터 보관
집합: 순서 X, 중복 X, 변경 O, 중괄호{}/set() 사용, 집합 연산/중복제거
딕셔너리: 키-값 O, 순서 X(키 기준), 키 중복 X, 변경 O, 중괄호{}(키:값) 사용
'''

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# 예시 그래프 및 호출
graph = {
    '1': ['2', '3'],
    '2': ['4'],
    '3': [],
    '4': []
}
dfs(graph, '1')  # 출력: 1 2 4 3