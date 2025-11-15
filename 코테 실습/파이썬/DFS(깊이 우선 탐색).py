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