#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.getPaths(root, '', res)
        return res
    
    def getPaths(self, root, path, res):
        if not root:
            return
        # 节点值加入当前路径
        path += str(root.val)
        # 如果当前节点是叶子节点，将当前路径加入结果集
        if root.left == None and root.right == None:
            res.append(path)
        # 如果当前节点不是叶子节点，继续遍历左子树和右子树。
        else:
            path += '->'
            self.getPaths(root.left, path, res)
            self.getPaths(root.right, path, res)


# @lc code=end

