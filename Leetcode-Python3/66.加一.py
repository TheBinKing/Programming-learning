#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """_summary_
        装逼优化
        Args:
            digits (List[int]): _description_

        Returns:
            List[int]: _description_
        """
        return list(map(int, str(int("".join(map(str, digits)))+1).zfill(len(digits))))

    def plusOne0(self, digits: List[int]) -> List[int]:
        """_summary_
        从后往前依次判断末尾是否为9 如果是 则去除
        Args:
            digits (List[int]): _description_

        Returns:
            List[int]: _description_
        """
        newlst = []
        while digits and digits[-1] == 9:
            digits.pop()
            newlst.append(0)
        if not digits:
            return [1] + newlst
        else:
            digits[-1] += 1
            return digits + newlst

