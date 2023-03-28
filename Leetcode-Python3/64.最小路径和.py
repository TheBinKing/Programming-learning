#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """_summary_
        动态规划，
        每次只能向右a[i][j+1]和向下a[i+1][j]
        注意两个边界，第一层和第一列，他们实现的路径是只能向下和向右才能到达，
        所以他们的最小值比较更加特殊。是只有一种情况的
        其他的就需要通过min的方法进行动态更新的。
        Args:
            grid (List[List[int]]): _description_

        Returns:
            int: _description_
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]


        
        
# @lc code=end

