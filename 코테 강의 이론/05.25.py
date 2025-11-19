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

def dfs(node, visited=None):
    if visited is None:
        visited = []
        is_first_call = True
    else:
        is_first_call = False

    visited.append(node)
    for adj in sorted(graph[node], reverse=False):  # 오름차순 정렬
        if adj not in visited:
            dfs(adj, visited)
    if is_first_call:
        print(visited)

# 사용 예시
dfs(1)  # [1, 2, 7, 6, 8, 3, 4, 5]
dfs(2)  # [2, 1, 3, 4, 5, 8, 7, 6]