# 닷 ㄱㄱ

# 시간 복잡도 O(N) 알고리즘 속에 가장 효율적인 코드는 아래와 같습니다. 코드의 전반적인 로직은 아래와 같습니다.
# 1. 음수들을 저장할 리스트와 양수들을 저장할 리스트를 초기화합니다.
#    각 리스트에 원본 배열의 요소를 추가하는 순서가 곧 상대적 순서를 보존하는 방법입니다.
# 2. 입력 배열의 각 요소를 for 반복문으로 순회합니다.
#    모든 요소를 단 한 번만 확인하므로 시간 복잡도는 O(N)이 됩니다.
# 3. 각 요소를 확인하여 음수인지 양수인지(또는 0인지) 판단합니다.
# 음수인 경우, negatives 리스트에 현재 순서대로 추가합니다.
# x >= 0 (양수 또는 0)
# 양수인 경우, positives 리스트에 현재 순서대로 추가합니다.
# 4. 모든 요소를 분리한 후, negatives 리스트 뒤에 positives 리스트를 합쳐서 반환합니다.
#    negatives = [-1, -2]
#    positives = [1, 3, 2]
#    결과 = [-1, -2, 1, 3, 2]
# 이건 진짜 효율적인 로직

def special_sort(arr):
    negatives = []
    positives = []

    for x in arr:
        if x < 0:
            negatives.append(x)
        else: 
            positives.append(x)
            
    return negatives + positives

# 입출력 예시 확인
input_arr = [-1, 1, 3, -2, 2]
print(f"입력: {input_arr}")
print(f"출력: {special_sort(input_arr)}") # 예상 출력: [-1, -2, 1, 3, 2]

input_arr_2 = [5, -3, 0, 7, -1, 4]
print(f"입력: {input_arr_2}")
print(f"출력: {special_sort(input_arr_2)}") # 예상 출력: [-3, -1, 5, 0, 7, 4]

input_arr_3 = [-10, -5, -1, -2]
print(f"입력: {input_arr_3}")
print(f"출력: {special_sort(input_arr_3)}") # 예상 출력: [-10, -5, -1, -2]

input_arr_4 = [10, 5, 1, 2]
print(f"입력: {input_arr_4}")
print(f"출력: {special_sort(input_arr_4)}") # 예상 출력: [10, 5, 1, 2]

# 버블 정렬 알고리즘 속에 풀 수 있는 코드는 아래와 같습니다.

# 1. 배열을 (배열 길이 - 1) 번 반복해서 순회합니다 (외부 루프).
#    각 패스(pass)마다 적어도 하나의 요소가 자신의 올바른 위치로 이동하게 됩니다.
#    'n'개의 요소에 대해 'n-1'번의 외부 반복이 필요합니다.
# i는 0부터 n-2까지 (총 n-1회)
# 한 패스 동안 교환이 일어났는지 확인하는 플래그 (최적화용)
# swapped = False # 현재 문제에서는 항상 교환이 일어날 수 있으므로 필수는 아님

# 2. 내부 루프에서는 인접한 두 요소를 비교하고 필요한 경우 교환합니다.
#    정렬된 부분이 늘어나므로, 매번 비교 범위를 줄일 수 있지만,
#    이 문제의 특정 조건(양수/음수)에서는 모든 패스를 끝까지 돌며
#    음수들이 앞으로 '버블링'되도록 하는 것이 직관적입니다.
# j는 0부터 (n-1-i)-1까지
# 매번 마지막 i개 요소는 이미 제자리를 찾았다고 가정 (최적화)

# 3. 교환 조건 확인: 현재 요소(arr[j])가 양수이고 다음 요소(arr[j+1])가 음수일 때만 교환
#    이렇게 하면 음수는 앞으로, 양수는 뒤로 이동하되,
#    같은 부호의 요소들 사이에서는 순서가 바뀌지 않아 안정성이 보장됩니다.
# 4. 조건에 맞으면 두 요소를 교환(swap)합니다.
# swapped = True

# 한 패스 동안 아무런 교환이 일어나지 않았다면 이미 정렬이 완료된 것이므로 루프를 중단 (최적화)
# if not swapped:
#    break

def special_sort_bubble(arr):
    n = len(arr)
    
    for i in range(n - 1): # 0 ~ n - 2까지 함, 즉 n - 1번 반복
        for j in range(n - 1 - i): 
            if arr[j] >= 0 and arr[j+1] < 0:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
    return arr

# 입출력 예시 확인
input_arr_1 = [-1, 1, 3, -2, 2]
print(f"입력: {input_arr_1}")
print(f"출력: {special_sort_bubble(input_arr_1)}") # 예상 출력: [-1, -2, 1, 3, 2]

input_arr_2 = [5, -3, 0, 7, -1, 4]
print(f"입력: {input_arr_2}")
print(f"출력: {special_sort_bubble(input_arr_2)}") # 예상 출력: [-3, -1, 5, 0, 7, 4]

input_arr_3 = [-10, -5, -1, -2]
print(f"입력: {input_arr_3}")
print(f"출력: {special_sort_bubble(input_arr_3)}") # 예상 출력: [-10, -5, -1, -2]

input_arr_4 = [10, 5, 1, 2]
print(f"입력: {input_arr_4}")
print(f"출력: {special_sort_bubble(input_arr_4)}") # 예상 출력: [10, 5, 1, 2]

input_arr_5 = [1, -1, 2, -2, 3, -3]
print(f"입력: {input_arr_5}")
print(f"출력: {special_sort_bubble(input_arr_5)}") # 예상 출력: [-1, -2, -3, 1, 2, 3]