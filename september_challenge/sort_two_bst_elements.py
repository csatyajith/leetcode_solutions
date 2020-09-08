from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Function to traverse the tree in-order
    def traverse_in_order(self, root, result):
        if root:
            self.traverse_in_order(root.left, result)
            result.append(root.val)
            self.traverse_in_order(root.right, result)
            return result

    # This solution uses the fact that in-order traversal of a BST yields a sorted list.
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        if not root1:
            return self.traverse_in_order(root2, [])
        if not root2:
            return self.traverse_in_order(root1, [])
        return sorted(self.traverse_in_order(root2, self.traverse_in_order(root1, [])))


if __name__ == '__main__':
    sol = Solution()
    r1 = TreeNode(2)
    r1.left = TreeNode(1)
    r1.right = TreeNode(4)
    r2 = TreeNode(1)
    r2.left = TreeNode(0)
    r2.right = TreeNode(3)
    print(sol.getAllElements(r1, r2))
