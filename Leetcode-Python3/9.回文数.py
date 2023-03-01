#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #通过转换成字符串的方式完成
        a=str(x)
        return a==a[::-1]
    def isPalindrome1(self, x: int) -> bool:
        #通过转换成字符串的方式完成
        a=str(x)
        return a==a[::-1]
    def isPalindrome0(self, x: int) -> bool:
        #通过转换成字符串的方式完成
        for i in range(0,len(str(x))-1):
            if str(x)[i]!=str(x)[-(i+1)]:
                return False
        return True
# @lc code=end


#0、1：
#   通过转换成python的字符串进行比较
