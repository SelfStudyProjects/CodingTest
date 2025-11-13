# A와 B가 이미 같은지 먼저 확인 (밀지 않아도 같은 경우: 0번 이동)
# A를 문자열에서 리스트로 변환 (pop, insert를 활용하기 위함)
# 파이썬에서 문자열은 불변(immutable)이기 때문에 변경 작업을 위해 리스트로 만듭니다.
# A의 길이 (즉, 몇 번까지 밀어볼 수 있는지 최대 횟수)
# len(A)번 밀면 다시 원래 A의 상태로 돌아오게 됩니다.
# 문자열을 민 횟수를 저장할 변수
# 0번 민 경우는 이미 위에서 처리했으므로 1부터 시작합니다.
# num_shifts (A의 길이)만큼 반복하며 한 칸씩 밀어봅니다.
# A의 길이와 B의 길이가 같다는 제한사항이 있으므로,
# A의 길이 = B의 길이 = num_shifts 입니다.
# for 루프 변수가 필요 없을 때는 _ (언더스코어) 사용
# 한 칸 밀었으니 횟수 증가
# - pop()을 활용해서 맨 뒤 요소 제거
# - insert()를 활용해서 새로운 요소 (제거된 마지막 요소)를 맨 앞에 추가
# 위 과정들을 수행 후, 현재 list_A가 B와 같은지 비교
# 리스트를 문자열로 다시 합쳐서 비교해야 합니다.
# 같으면 현재까지 민 횟수 반환
# for 반복문 다 수행했는데 동일한 값이 없으면 (즉, 위에서 return 되지 않으면)
# -1 반환

def solution(A, B):
    if A == B:
        return 0
    list_A = list(A) 
    list_B = list(B)
    num_shifts = len(A)
    shift_count = 0 
    for _ in range(num_shifts):
        shift_count += 1
        last_char = list_A.pop()
        list_A.insert(0, last_char) 
        
        if list_A == list_B:
            return shift_count
    return -1