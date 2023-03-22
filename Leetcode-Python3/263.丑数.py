#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        """
        根据丑数的判断，对每个质数元素进行判断
        """
        if n==0:
            return False
        for i in [2,3,5]:
            while n%i==0:
                n/=i
        return n==1
# @lc code=end

