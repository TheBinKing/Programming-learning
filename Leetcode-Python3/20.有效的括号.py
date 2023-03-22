#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        _dic={')':'(','}':'{',']':'['}
        _stack=[]
        for c in s:
            if c not in _dic:
                _stack.append(c)
            elif not _stack or _dic[c]!=_stack.pop():
                return False
        return not _stack
    def isValid0(self, s: str) -> bool:
        stack=[]
        n=len(s)
        for i in range(n):
            if  stack:
                if s[i]==stack[-1]:
                    stack.pop[-1]
                else:
                    stack.append(s[i])
                continue
            stack.append(s[i])
        if stack:return False
        else:return True
# @lc code=end

