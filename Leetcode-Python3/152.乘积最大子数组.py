#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """_summary_
        动态规划问题，唯一需要注意的问题就是，最小值有可能乘了以后变成最大值（eg负数）
        Args:
            nums (List[int]): _description_

        Returns:
            int: _description_
        """
        if not nums: return 
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res

# @lc code=end

