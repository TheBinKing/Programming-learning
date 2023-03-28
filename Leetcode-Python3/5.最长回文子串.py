#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """_summary_
        常规动态规划
        1.特判
        2.初始化参数，最大长度，dp数组
        3.判断长度为1都为回文，长度为2判断是否为回文
        3.长度为3的进行遍历[3,n+1)
        Args:
            s (str): _description_

        Returns:
            str: _description_
        """
        if(not s or len(s)==1):
            return s
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        max_len=1
        start=0
        for i in range(n):
            dp[i][i]=True
            if(i<n-1 and s[i]==s[i+1]):
                dp[i][i+1]=True
                start=i
                max_len=2
        for l in range(3,n+1):
            for i in range(n+1-l):
                r=i+l-1
                if(s[i]==s[r] and dp[i+1][r-1]):
                    dp[i][r]=True
                    start=i
                    max_len=l
        return s[start:start+max_len]

    def longestPalindrome0(self, s):
        """_summary_
        设置一个最长回文子串res，要寻找最长的回文子串，所以其长度只会越来越长
        遍历整个数组，i为指针。根据i的位置向前找回文子串，
        这里要注意，我们只需要去找长度大于res的回文子串就可以了，
        所以定位到回文子串的开头的前一位应该是：start = i - len(s) - 1, 
        但是start可能会小于0，因此做一个截断start = max(0, i-len(s)-1)。

        根据选定的回文子串的索引范围，对字符串做切片，并判断是否是回文子串。
        这里需要注意，此时分为开头讨论的两种情况，
        即奇数个回文子串和偶数个回文子串，之后把寻找到的回文子串重新赋值给res，
        这样res的长度会随着指针的遍历越来越大，遍历结束后，res即为最长回文子串。

        Args:
            s (_type_): _description_

        Returns:
            _type_: _description_
        """
        res = ''
        for i in range(len(s)):
            start = max(i - len(res) -1, 0)
            temp = s[start: i+1]
            if temp == temp[::-1]:
                res = temp
            else:
                temp = temp[1:]
                if temp == temp[::-1]:
                    res = temp
        return res
# @lc code=end

