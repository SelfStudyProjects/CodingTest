# 가장 거리가 짧은 것의 쌍을 출력
# 다시

'''
첫번째 예시에서
# if diff not in diff_map: 이 부분이 없다고 가정하면:
# 바로 'diff_map[diff].append(pair)'부분에서 에러가 발생!
# diff_map에 '2'라는 키가 없는데 diff_map['2']를 호출해서 리스트를 찾으려 했기 때문

'''

def closest_pair_all_pairs(S):
    diff_map = {}
    n = len(S)
    
    for i in range(n-1):
        for j in range(i+1, n):
            diff = abs(S[i] - S[j])
            if diff not in diff_map:
                diff_map[diff] = []
            diff_map[diff].append((S[i], S[j])) # 거기에 맞게 튜플 추가, 튜플은 딕셔너리의 값에 해당
    
    min_diff = sorted(diff_map.keys())[0]  # 최소 차이값
    return diff_map[min_diff][0]            # 최소 차이 쌍 중 첫번째 쌍 반환
    # 최소 차이가 나는 쌍들이 여러 개일 수 있기 때문에 그거를 고려해서 하는 것

# 위의 것이 내가 적은 코드 전문, 아래는 훨씬 직관적이고 간단한 코드 전문

def closest_pair_adjacent(S):
    min_diff = float('inf')
    # 가장 작은 거리를 찾을 건데 처음엔 어떤 숫자보다도 무한대로 큰 값을 넣어서 초기화, 양의 무한대
    min_pair = None
    
    for i in range(len(S) - 1):
        diff = abs(S[i] - S[i+1])
        if diff < min_diff:
            min_diff = diff
            min_pair = (S[i], S[i+1]) # '()'은 튜플

    return min_pair

# 예시
S = [1, 3, 4, 8, 13, 17, 20]
print(closest_pair_all_pairs(S))  # 출력: (3, 4)