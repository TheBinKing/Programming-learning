#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        """_summary_
        枚举特殊情况，进行拆分计算求和，方法0的装逼版本
        Args:
            s (str): _description_

        Returns:
            int: _description_
        """
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))

    
    def romanToInt0(self, s: str) -> int:
        """_summary_
        枚举判断是否存在特殊情况，如果不存在就单独处理，针对判断情况进行求和处理
        Args:
            s (str): _description_

        Returns:
            int: _description_
        """
        d = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90,  'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        result = 0
        i = 0
        while i < len(s):
            #查看当前位和下一位的字符
            str1 = s[i:i+2]  
            #如果当前位置是特殊情况，那么返回其在字典中对应值，并且下一次从特殊字符之后一位开始索引
            if str1 in d: 
                result += d.get(str1) 
                i += 2
            #如果当前位不是特殊情况，那么只返回当前位的数值
            else:
                result += d[s[i]] 
                i += 1
        return result
# @lc code=end

