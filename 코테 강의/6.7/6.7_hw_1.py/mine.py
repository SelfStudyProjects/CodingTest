import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)] 

    for a, b, c in road:
        graph[a].append((b, c))  
        graph[b].append((a, c))  

    dist = [float('inf')] * (N + 1)
    dist[1] = 0 

    heap = []
    heapq.heappush(heap, (0, 1)) 

    while heap:
        current_dist, now = heapq.heappop(heap)

        if dist[now] < current_dist:
            continue

        for next_node, cost in graph[now]:
            new_dist = current_dist + cost
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    answer = sum(1 for d in dist if d <= K)

    return answer