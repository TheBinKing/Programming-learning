#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """_summary_
        整体思路其实和上面差不多
        dp[i][j] 表示到从上到下走到i,j位置最小路径的值.

        动态方程: dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + triangle[i][j]
        dp时候每次只用到上一层数据,如果我们倒着,从底向上可以优化成O(n)空间
        Args:
            triangle (List[List[int]]): _description_

        Returns:
            int: _description_
        """
        row = len(triangle)
        dp = [0] * row
        for i in range(len(triangle[-1])):
            dp[i] = triangle[-1][i]
        #print(dp)
        for i in range(row - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]        


# @lc code=end

