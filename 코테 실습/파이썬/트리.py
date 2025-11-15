'''
* 문제 설명
이진 탐색 트리(BST)의 루트 노드와 정수 target이 주어질 때, 트리에서 target 값이 존재하면 True, 없으면 False를 반환하는 함수를
작성하세요. 이진 탐색 트리의 특성은 각 노드의 왼쪽 서브트리 값은 노드 값보다 작고, 오른쪽 서브트리 값은 노드 값보다
크다는 점입니다.

알고리즘/자료구조 구체적 설명 — 이진 탐색 트리(BST)와 검색

정의: 이진 탐색 트리는 각 노드가 두 자식(왼쪽/오른쪽)을 가지며, 왼쪽 서브트리의 모든 값은 노드 값보다 작고 오른쪽
서브트리의 모든 값은 노드 값보다 크도록 유지되는 이진 트리.

검색 원리: 루트부터 시작해 target과 현재 노드 값을 비교하고, 작으면 왼쪽, 크면 오른쪽으로 내려가며 탐색(이진 탐색의 트리 버전).

시간복잡도: 평균 O(h) = O(log n) (균형 트리일 때), 최악 O(n) (심하게 한쪽으로 치우친 경우, 예: 정렬된 데이터를 순차적으로
삽입했을 때). h는 트리 높이, n은 노드 수.

공간복잡도: 재귀 호출 스택 O(h)
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