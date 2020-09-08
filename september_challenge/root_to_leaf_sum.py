# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse_tree(self, node, num, nums):
        if node:
            num += str(node.val)
            if not node.left and not node.right:
                nums.append(num)
            else:
                self.traverse_tree(node.left, num, nums)
                self.traverse_tree(node.right, num, nums)
        return nums

    def sumRootToLeaf(self, root: TreeNode) -> int:
        nums = self.traverse_tree(root, "", [])
        sum_d = 0
        for num in nums:
            num_d = 0
            for i in range(len(num)):
                num_d += int(num[-(i + 1)]) * (2 ** i)
            sum_d += num_d

        print(nums)
        return sum_d


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    print(sol.sumRootToLeaf(root))
