#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        双指针
        """
        p1,p2=0,0
        s_len,t_len=len(s),len(t)
        
        
        pass
    def isSubsequence0(self, s: str, t: str) -> bool:
        """
        循环+切片
        有点像双指针方法对抽象优化
        18/18 cases passed (36 ms)
        Your runtime beats 81.16 % of python3 submissions
        Your memory usage beats 73.94 % of python3 submissions (15 MB)
        """
        for i in s:
            if i in t:
                t=t[t.index(i)+1:]
            else:
                return False
        return True
# @lc code=end

