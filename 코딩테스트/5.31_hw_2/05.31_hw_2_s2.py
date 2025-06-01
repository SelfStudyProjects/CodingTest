from itertools import combinations
from collections import deque
import copy
def bfs(N, M, x, y, map_):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(x, y)])

    while queue:
        current = queue.popleft()

        for d in directions:
            new_x = current[0] + d[0]
            new_y = current[1] + d[1]
            if 0 <= new_x < N and 0 <= new_y < M:
                if map_[new_x][new_y] == '0':
                    queue.append((new_x, new_y))
                    map_[new_x][new_y] = '2'
                    
N, M = map(int, input().split())
map_ = []
zero = []
virus = []
max_safe = 0
for i in range(N):
    line = list(input().split())
    map_.append(line)
    for j, num in enumerate(line):
        if num == '0':
            zero.append((i, j))
        if num == '2':
            virus.append((i, j))

for walls in combinations(zero, 3):
    safe = 0
    copied_map = copy.deepcopy(map_)
    for wall in walls:
        copied_map[wall[0]][wall[1]] = '1'
    for v in virus:
        bfs(N, M, v[0], v[1], copied_map)
    for i in copied_map:
        safe += i.count('0')
    max_safe = max(max_safe, safe)
print(max_safe)