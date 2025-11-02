# 시간 복잡도 O(N) 알고리즘 속에 가장 효율적인 코드는 아래와 같습니다.

def special_sort(arr):
    # 1. 음수들을 저장할 리스트와 양수들을 저장할 리스트를 초기화합니다.
    #    각 리스트에 원본 배열의 요소를 추가하는 순서가 곧 상대적 순서를 보존하는 방법입니다.
    negatives = []
    positives = []

    # 2. 입력 배열의 각 요소를 for 반복문으로 순회합니다.
    #    모든 요소를 단 한 번만 확인하므로 시간 복잡도는 O(N)이 됩니다.
    for x in arr:
        # 3. 각 요소를 확인하여 음수인지 양수인지(또는 0인지) 판단합니다.
        if x < 0:
            # 음수인 경우, negatives 리스트에 현재 순서대로 추가합니다.
            negatives.append(x)
        else: # x >= 0 (양수 또는 0)
            # 양수인 경우, positives 리스트에 현재 순서대로 추가합니다.
            positives.append(x)
            
    # 4. 모든 요소를 분리한 후, negatives 리스트 뒤에 positives 리스트를 합쳐서 반환합니다.
    #    negatives = [-1, -2]
    #    positives = [1, 3, 2]
    #    결과 = [-1, -2, 1, 3, 2]
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

