"""
date:20231128
author:lhz
note:LowestCommonAncestor
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root, p, q):
    if not root:
        return None
    # 如果当前节点是p或q之一，则当前节点就是它们的最近公共祖先
    if root == p or root == q:
        return root
    # 递归查找左右子树
    left_ancestor = lowestCommonAncestor(root.left, p, q)
    right_ancestor = lowestCommonAncestor(root.right, p, q)

    # 如果左右子树分别包含p和q，则当前节点是它们的最近公共祖先
    if left_ancestor and right_ancestor:
        return root
    # 否则，返回非空的那个子树的结果（包含p或q）
    return left_ancestor if left_ancestor else right_ancestor


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

p = root.left.left
q = root.left.right

result = lowestCommonAncestor(root, p, q)
print(result.val)
