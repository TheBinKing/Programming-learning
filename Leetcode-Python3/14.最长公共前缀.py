#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#https://leetcode.cn/problems/longest-common-prefix/solutions/288575/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        十分巧妙的方法，用了字符串排序的方法进行简化处理。
        
        
        124/124 cases passed (40 ms)
        Your runtime beats 57.17 % of python3 submissions
        Your memory usage beats 76.6 % of python3 submissions (15 MB)
        
        
        124/124 cases passed (36 ms)
        Your runtime beats 79.82 % of python3 submissions
        Your memory usage beats 31.93 % of python3 submissions (15.1 MB)
        神奇的现场，差别仅仅在于range(x)->速度快,range(0,x)->存储好
        """
        if not strs: return ""
        maxstr=max(strs)
        minstr=min(strs)
        for i in range(0,len(minstr)):
            if maxstr[i] !=minstr[i]:
                return minstr[:i]
        return minstr
                    
                
    
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        """
        124/124 cases passed (40 ms)
        Your runtime beats 57.17 % of python3 submissions
        Your memory usage beats 56.3 % of python3 submissions (15.1 MB)
        """
        n = len(strs)
        i=0 
        while i<len(strs[0]):
            for j in range(0,n):
                if i>=len(strs[j]) or strs[j][i]!=strs[0][i]:
                    return strs[0][:i]
            i+=1
        return strs[0][:i]
                    
                

    
    def longestCommonPrefix0(self, strs: List[str]) -> str:
        """
        透过一个循环去从头开始对每个字符串进行对比。
        通过设定几个判断条件进行控制：
            1.长度。如果某个字符串和需要进行比对的长度位不同说明达到最大前缀长度。
            2.是否相等。如果不相等则说明达到最大前缀长度。
            3.此外，做了一些特殊例子的补丁。（全空列表等）
        
        124/124 cases passed (40 ms)
        Your runtime beats 57.17 % of python3 submissions
        Your memory usage beats 38.65 % of python3 submissions (15.1 MB)
        """
        tag=1
        num=0
        while(1):
            alp=''
            for str_ in strs:
                if len(str_)<=num:
                    tag=0
                    break
                elif len(str_)==0:
                    tag=0
                    break
                else:
                    if alp=='':
                        alp=str_[num]
                    if str_[num]!=alp:
                        tag=0
                        break
            num+=1
            if tag==0:
                if num==0:
                    return ''
                else:
                    return strs[0][:num-1]

                
# @lc code=end

