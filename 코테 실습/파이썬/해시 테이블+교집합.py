'''
문제 설명
정수(또는 해시 가능한 값)로 이루어진 두 리스트 arr1, arr2가 주어질 때, 두 리스트의 교집합(공통 원소)을
효율적으로 찾아 리스트로 반환하세요. 결과의 순서는 문제 요구에 따라 유지하거나(예: arr2 순서 유지) 정렬할 수 있습니다.
'''

def find_common_elements(arr1, arr2):
    hash_set = set(arr1)                       # arr1의 원소를 해시셋에 저장
    result = [x for x in arr2 if x in hash_set]# arr2 순서 유지하면서 공통 원소 수집
    return result

print(find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]