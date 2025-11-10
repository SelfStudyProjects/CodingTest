import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        if cur_dist > distances[cur_node]:
            continue

        for neighbor, weight in graph[cur_node]:
            distance = cur_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('C', 1)],
    'C': []
}

print(dijkstra(graph, 'A'))  # {'A': 0, 'B': 2, 'C': 3}