# 가장 거리가 짧은 것의 쌍을 출력
'''
통계학적으로 NC2를 구할 수 있는 방법의?
난 이거를 위해 이중 for 반복문 이용?하려고 함
첫번째 for 반복문을 0에서 시작해서 전체 요소 개수(n) 기준 n - 1까지
가게끔 하고, 두번째 for 반복문은 1에서 시작해서 n까지 가게끔
하는 걸로. 마치 아래와 같이
i = 0, y = 1
for i in n - 1 :
    for y in n :
이런 느낌으로?
그리고 딕셔너리를 활용해야 할 듯. 참고로 i, y는
리스트 S의 요소의 인덱스로 활용
그 인덱스 기반으로 값 도출하고, 2개의 값들을 '-'해서 차익 구하고
이거를 '키'로 하고, 2개의 요소들을 리스트로 묶어서 '값'으로 삼기
그리고 그 '키'들을 따로 배열로 append 메소드 이용해서 추가하고, 해당 배열
기준으로 오름차순 정렬 sorted(reversed = False)하기, 그리고 인덱스 0에 해당되는
값을 도출해서 이거를 생성한 딕션너리 기준으로 값을 도출해서 return하기, 다만
'''

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

# 위의 것이 내가 적은 코드 전문, 아래는 훨씬 직관적이고 간단한 코드 전문

def closest_pair_adjacent(S):
    min_diff = float('inf')
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