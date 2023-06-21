#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
import sys
# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        """_summary_
        存储消耗更小，但是速度更慢
        Args:
            x (int): _description_

        Returns:
            int: _description_
        """
        sign = 1
        if x < 0:
            x = abs(x)
            sign = -1
        ret = int(str(x)[::-1]) * sign
        if -2**31 <= ret <= 2 **31 -1:
            return ret
        else:
            return 0

    def reverse1(self, x: int) -> int:
        """_summary_
        方法0的简洁版本
        
        Args:
            x (int): _description_
        Returns:
            int: _description_  
        Your runtime beats 80.05 % of python3 submissions
        Your memory usage beats 18.62 % of python3 submissions (15 MB)
        """
        res=int(str(x)[::-1]) if x>=0 else -int(str(x)[1:][::-1])
        return 0 if res>pow(2,31)-1 or res<-pow(2,31) else res
    
    def reverse0(self, x: int) -> int:
        """_summary_
        最简单的类型转换。
        -首先进行正负判断
        -int转换成str类型
        -字符串翻转
        -类型转换
        -判断转换后的内容是否超过边界
        Args:
            x (int): _description_
        Returns:
            int: _description_
        """
        if x >= 0:
            result=int(str(x)[::-1])
            return result if result<(2**31 - 1) else 0
        else:
            result=-int(str(abs(x))[::-1])
            return result if result>(-2**31) else 0
# @lc code=end

