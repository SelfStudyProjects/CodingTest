# 가장 거리가 짧은 것의 쌍을 출력
# 다시

def closest_pair_all_pairs(S):
    diff_map = {}
    n = len(S)
    
    for i in range(n-1):
        for j in range(i+1, n):
            diff = abs(S[i] - S[j])
            if diff not in diff_map:
                diff_map[diff] = []
            diff_map[diff].append((S[i], S[j]))
    
    min_diff = sorted(diff_map.keys())[0]  # 최소 차이값
    return diff_map[min_diff][0]            # 최소 차이 쌍 중 첫번째 쌍 반환
    # 최소 차이가 나는 쌍들이 여러 개일 수 있기 때문에 그거를 고려해서 하는 것

# 위의 것이 내가 적은 코드 전문, 아래는 훨씬 직관적이고 간단한 코드 전문

def closest_pair_adjacent(S):
    min_diff = float('inf')
    # 가장 작은 거리를 찾을 건데 처음엔 어떤 숫자보다도 무한대로 큰 값을 넣어서 초기화하는 거야.
    min_pair = None
    
    for i in range(len(S) - 1):
        diff = abs(S[i] - S[i+1])
        if diff < min_diff:
            min_diff = diff
            min_pair = (S[i], S[i+1])

    return min_pair

# 예시
S = [1, 3, 4, 8, 13, 17, 20]
print(closest_pair_all_pairs(S))  # 출력: (3, 4)