#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic=dict()
        for i in range(len(nums)):
            if (target-nums[i]) not in dic:
                dic[nums[i]]=i
            else:
                return  [i,dic[target-nums[i]]]
# @lc code=end

