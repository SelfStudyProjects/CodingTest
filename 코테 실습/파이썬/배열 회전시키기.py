'''

### ✨ Python 리스트 메서드 가이드
다음은 `numbers` 리스트를 다루는 데 사용된 주요 메서드들이야.

---

#### 1. `list.pop()`

*   **역할**: 리스트에서 특정 위치의 요소를 **제거**하고 그 **제거된 요소를 반환**합니다. (원본 리스트 변경 O)
*   **왜 사용?**: 배열 회전 문제에서 특정 요소를 리스트에서 빼내 다른 곳에 다시 넣어야 할 때 아주 유용하게 쓰입니다. 예를 들어, `numbers.pop()`으로 맨 끝 요소를 빼거나, `numbers.pop(0)`으로 맨 앞 요소를 뺄 수 있죠.
*   **어떻게 구현?**:
    *   `list.pop()`: 인자가 없으면 리스트의 **맨 마지막 요소**를 제거하고 반환합니다.
    *   `list.pop(index)`: `index` 위치의 요소를 제거하고 반환합니다.
*   **예시**:
    ```python
    my_list = [10, 20, 30, 40]
    last = my_list.pop()    # last = 40, my_list = [10, 20, 30]
    first = my_list.pop(0)  # first = 10, my_list = [20, 30]
    ```

---

#### 2. `list.insert(index, element)`

*   **역할**: 리스트의 **특정 `index` 위치에 `element`를 삽입**합니다. 기존 요소들은 한 칸씩 뒤로 밀립니다. (원본 리스트 변경 O)
*   **왜 사용?**: 리스트의 중간이나, 특히 맨 앞에 요소를 추가하고 싶을 때 사용합니다. `right` 회전 시 마지막 요소를 맨 앞(`index=0`)에 삽입하는 데 쓰였죠.
*   **어떻게 구현?**: `list.insert(index, element)` 형태로 사용합니다.
    *   `index=0`이면 맨 앞에 삽입됩니다.
    *   `index=-1`이면 마지막 요소 *바로 앞*에 삽입됩니다.
    *   `index`가 리스트의 현재 길이보다 크면, 맨 마지막에 추가됩니다.
*   **예시**:
    ```python
    my_list = [10, 20, 40]
    my_list.insert(0, 5)    # my_list = [5, 10, 20, 40]
    my_list.insert(2, 25)   # my_list = [5, 10, 25, 20, 40]
    my_list.insert(-1, 35)  # my_list = [5, 10, 25, 20, 35, 40] (마지막 40 앞에 삽입)
    ```

---

#### 3. `list.append(element)`

*   **역할**: 리스트의 **맨 마지막에 `element`를 추가**합니다. (원본 리스트 변경 O)
*   **왜 사용?**: `left` 회전 시 첫 요소를 제거한 후, 그 요소를 리스트의 맨 뒤에 붙여야 할 때 사용합니다. `insert(-1, ...)`과 달리 명확하게 맨 뒤에 추가됩니다.
*   **어떻게 구현?**: `list.append(element)` 형태로 사용합니다.
*   **예시**:
    ```python
    my_list = [10, 20, 30]
    my_list.append(40)    # my_list = [10, 20, 30, 40]
    ```
'''

def solution(numbers, direction):
    if direction == "right":
        numbers.insert(0, numbers[-1])
        numbers.pop()
    else:
        num = numbers.pop(0)
        numbers.append(num)
    return numbers
     