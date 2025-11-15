'''

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