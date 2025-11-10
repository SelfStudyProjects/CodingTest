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

'''
문제 설명
가중치(비음수)를 가진 방향 그래프(또는 무방향 그래프)와 시작 정점 start가 주어질 때, start로부터 각 정점까지의 최단 거리를 구해 딕셔너리 형태로 반환하세요. (만약 어떤 정점에 도달 불가능하면 거리는 무한으로 남김)

제한사항(예시)

모든 간선의 가중치는 0 이상(음수 가중치가 있으면 다익스트라 사용 불가)
그래프는 인접 리스트 형태로 제공: graph[node] = [(neighbor, weight), ...]
입출력 예

graph = {'A': [('B', 2), ('C', 5)], 'B': [('C', 1)], 'C': []}, start='A' → {'A':0, 'B':2, 'C':3}

라인별 why — how — what 설명

import heapq

what: 파이썬 표준 라이브러리 heapq 모듈(최소 힙 사용)을 가져옴.
why: 매 단계에서 "가장 작은 거리"를 가진 노드를 빠르게 추출해야 해서 우선순위 큐가 필요함.
how: heappush, heappop API 사용.

def dijkstra(graph, start):

what: 다익스트라 알고리즘을 구현한 함수 선언.
why: 시작점으로부터 각 정점까지의 최단 거리를 계산하려고 캡슐화.
how: graph는 인접 리스트를 가정(딕셔너리).

distances = {node: float('inf') for node in graph}

what: 각 노드의 거리를 무한대로 초기화한 딕셔너리.
why: 아직 도달하지 않은 노드를 '무한'으로 표시해 이후 더 작은 값으로 갱신되도록 함.
how: dict comprehension 사용.

distances[start] = 0

what: 시작 노드의 거리는 0으로 설정.
why: 출발점이므로 거리 0.
how: 딕셔너리 값 대입.

queue = [(0, start)]

what: (거리, 노드) 튜플을 담는 힙을 초기화.
why: (거리, 노드)로 넣으면 첫 요소(거리)를 기준으로 최소 힙이 작동.
how: 리스트 형태로 초기값 설정.

while queue:

what: 힙이 빌 때까지 반복.
why: 아직 처리할 후보 노드가 남아 있기 때문에 계속 탐색.
how: 파이썬의 while 반복문.

cur_dist, cur_node = heapq.heappop(queue)

what: 현재 후보 중 가장 작은 거리의 항목을 꺼냄.
why: 다익스트라는 최소 거리 노드를 확정적으로 처리하는 그리디 알고리즘.
how: heappop으로 (distance, node) 튜플 추출.

if cur_dist > distances[cur_node]:

what: 꺼낸 항목이 오래된 값(이미 더 작은 값으로 갱신된 경우)이면 무시.
why: 힙에는 동일 노드의 여러 엔트리가 들어갈 수 있어 오래된 항목을 처리하지 않기 위함.
how: 비교 후 continue.

for neighbor, weight in graph[cur_node]:

what: 현재 노드의 인접 간선(이웃, 가중치)을 순회.
why: 이웃의 거리 후보를 계산해서 갱신(relax)해야 함.
how: 인접 리스트 순회.

distance = cur_dist + weight

what: 출발점→현재노드→이웃으로 가는 후보 거리 계산.
why: 경유 비용 합산은 최단 거리 계산의 기본.
how: 덧셈 연산.

if distance < distances[neighbor]:

what: 후보 거리가 기존 기록보다 작으면 갱신 필요.
why: 더 짧은 경로를 찾았으므로 갱신해야 이후 단계에서 이 값이 반영됨.
how: 조건문으로 비교, 참이면 아래 갱신 수행.

distances[neighbor] = distance

what: 이웃 노드의 거리를 갱신.
why: 이후 탐색 시 이 갱신된 거리를 사용하기 위해.
how: 딕셔너리 대입.

heapq.heappush(queue, (distance, neighbor))

what: 갱신된 이웃 노드를 힙에 삽입.
why: 추후 가장 작은 거리 후보로 꺼내기 위해 우선순위 큐에 넣음.
how: heappush 사용.

return distances

what: 모든 처리가 끝난 뒤 최종 거리 딕셔너리 반환.
why: 호출자에게 결과를 전달.
how: return.

알고리즘/자료구조 구체적 설명 — 다익스트라와 우선순위 큐

다익스트라 알고리즘:

목적: 단일 출발점에서 모든 정점까지의 최단 거리 계산(비음수 가중치 그래프).
핵심 아이디어: 그리디하게 현재까지 발견한 가장 짧은 거리 노드를 하나씩 확정하고, 그 노드를 통해 이웃들의 거리를 완화(relax)시킴.
제한: 간선 가중치가 음수이면 부정확. 음수 간선이 있으면 벨만-포드 사용.
자료구조:

인접 리스트: graph[node] = [(neighbor, weight), ...] — 희소 그래프에 메모리 효율적.
우선순위 큐(힙): 현재 처리할 노드를 최소 거리 기준으로 빠르게 선택하기 위해 사용. 파이썬의 heapq는 최소 힙을 제공.
distances 딕셔너리/배열: 각 노드의 현재 최단거리 기록.
시간복잡도:

힙(우선순위 큐) 사용 시: O((V + E) log V) ≈ O(E log V) (V: 정점 수, E: 간선 수).
만약 힙을 사용하지 않고 매번 선형으로 최소값을 찾으면 O(V^2).
구현상의 유의점:

힙에 동일 노드가 여러 항목으로 들어갈 수 있음(갱신 시마다 push). 따라서 pop한 후 현재 distances와 비교해 오래된 항목이면 무시하는 체크가 필요함.
노드를 정수로 매핑하면 리스트 기반 distances로 더 빠르게 구현 가능(딕셔너리보다 인덱스 접근이 빠름).
'''