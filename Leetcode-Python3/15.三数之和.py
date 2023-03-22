#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            if i+2<=len(nums)-1:
                if nums[i]+nums[i+1]+nums[i+2]==0:
                    temp=[nums[i],nums[i+1],nums[i+2]]
                    res.append(temp)
            else:
                return res
# @lc code=end

