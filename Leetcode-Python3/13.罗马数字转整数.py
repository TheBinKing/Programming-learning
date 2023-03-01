#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dic={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000}
        biggest_roma='I'
        before_before=s[0]
        pre_num=0
        num_all=0
        for i in range(len(s)):
            
        for i in range(len(s)):
            if roman_dic[s[i]]>roman_dic[biggest]:
                biggest=s[i]
                pre_num+=roman_dic[s[i]]
            else:
                pass
            
# @lc code=end

