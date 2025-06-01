from collections import deque
def bfs(start, city, K, result):
 visited = [False] * len(city)
 queue = deque([(start, 0)]) # (위치, 거리)
    visited[start - 1] = True
    while queue:
        current = queue.popleft()
        if current[1] == K:
            result.append(current[0])
       
        if current[1] > K:
            break
       
        for next_city in city[current[0] - 1]:
            if not visited[next_city - 1]:
                queue.append((next_city, current[1] + 1))
                visited[next_city - 1] = True
    return result        
N, M, K, X = map(int, input().split())
city = [[] for _ in range(N)]
for i in range(M):
    src, dst = map(int, input().split())
    city[src - 1].append(dst)
    city[dst - 1].append(src)
result = sorted(bfs(X, city, K, []))
if result:
    for r in result:
        print(r)
else:
    print(-1)