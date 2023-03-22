#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        windows,res=[],[]
        for i,x in enumerate(nums):
            if i>=k and windows[0]<i-k:
                windows.pop(0)
            while windows and nums[windows[-1]]<=x:
                windows.pop()
            windows.append(i)
            if i > k-1:
                #windows[0]永远存着最大的值
                res.append(nums[windows[0]])
        return res 
        
    def maxSlidingWindow0(self, nums: List[int], k: int) -> List[int]:
        duilie=[]
        num=0
        for i in range(k):
            duilie.append[nums[num+i]]
        while 1:

                
# @lc code=end

