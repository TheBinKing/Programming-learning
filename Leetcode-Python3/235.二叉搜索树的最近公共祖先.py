#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果当前节点的值 node.val 大于 p 和 q 的值，那证明 p 和 q 在 node 的左子树中
        if root.val > p.val and root.val > q.val:
            # 遍历左子树
            return self.lowestCommonAncestor(root.left, p, q)
        # 如果当前节点的值 node.val 小于 p 和 q 的值，那证明 p 和 q 在 node 的右子树中
        if root.val < p.val and root.val < q.val:
            # 遍历右子树
            return self.lowestCommonAncestor(root.right, p, q)
        # 如果当前节点的值 node.val 在 [p, q] 之间，那 node 就是最近公共祖先。
        return root
# @lc code=end

