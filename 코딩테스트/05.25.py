# 그래프 인접 리스트 표현
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

visited = []

def dfs(node):
    visited.append(node)
    for adj in sorted(graph[node], reverse=False):  # 오름차순 정렬
        if adj not in visited:
            dfs(adj)

dfs(1)
print(visited)  # [1, 2, 7, 6, 8, 3, 4, 5]