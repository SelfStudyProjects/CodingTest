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