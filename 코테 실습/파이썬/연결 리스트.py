'''
문제 설명
단일 연결 리스트의 특정 노드 뒤에 새 노드를 삽입하는 함수를 작성하세요.
주어진 노드 node의 바로 다음 위치에 값 new_val을 가지는 새 노드를 삽입해야 합니다.

print(curr.val, end=' -> ' if curr.next else '\n')
동작: print 함수를 사용하여 현재 curr가 가리키는 노드의 val 속성(값)을 출력합니다.
핵심: end 매개변수를 사용해서 출력 방식(1 -> 2 -> 3)을 조절합니다.
if curr.next else '\n': 조건부 표현식입니다.
만약 curr.next가 None이 아니면 (즉, 다음 노드가 존재하면, True), 출력 끝에 ' -> ' 문자열을 붙입니다.
만약 curr.next가 None(False)이면 (마지막 노드이면), 출력 끝에 줄 바꿈 문자 \n을 붙여 다음 줄로 이동시킵니다.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_after(node, new_val):
    new_node = Node(new_val)
    new_node.next = node.next
    node.next = new_node

# 예시
head = Node(1)
head.next = Node(3)
insert_after(head, 2)

# 결과 출력: 1 → 2 → 3
curr = head
while curr:
    print(curr.val, end=' -> ' if curr.next else '\n')
    curr = curr.next