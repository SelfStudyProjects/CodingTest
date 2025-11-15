'''
문제 설명
이진 탐색 트리(BST)의 루트 노드와 정수 target이 주어질 때, 트리에서 target 값이 존재하면 True, 없으면 False를 반환하는 함수를
작성하세요. 이진 탐색 트리의 특성은 각 노드의 왼쪽 서브트리 값은 노드 값보다 작고, 오른쪽 서브트리 값은 노드 값보다
크다는 점입니다.
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search_bst(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    elif target < root.val:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)

# 예시 트리 생성 및 호출
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
print(search_bst(root, 3))  # True
print(search_bst(root, 7))  # False