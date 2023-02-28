#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0 or x ==1:
            return x
        for i in range(x+1):
            if i*i==x:
                return i
            elif i*i>x:
                return i-1
    def mySqrt0(self, x: int) -> int:
        if x ==0 or x ==1:
            return x
        for i in range(x+1):
            if i*i==x:
                return i
            elif i*i>x:
                return i-1 
# @lc code=end

#

