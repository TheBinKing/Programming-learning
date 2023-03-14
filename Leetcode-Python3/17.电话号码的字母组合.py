#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """_summary_
        回溯法，通常在二叉树中被使用，更广义上来说，可以处理类树状结构或树形问题
        类似于先遍历到每一个叶子节点，然后返回的时候依次添加上中间的内容。
        Args:
            digits (str): _description_

        Returns:
            List[str]: _description_
        """
        if not digits:
            return []
        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
        def backtrack(combination,next_digits):
            if len(next_digits) == 0:
                return output.append(combination)
            else:
                for letter in phone[next_digits[0]]:
                    backtrack(combination+letter,next_digits[1:])
               
        output = []
        if digits:
            backtrack('',digits)
        return output




# @lc code=end

