#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """_summary_
        单调栈
        Args:
            heights (List[int]): _description_

        Returns:
            int: _description_
        """
        heights.insert(0,0)
        heights.append(0)
        maxarea=0
        stack=[]
        for i,value in enumerate(heights):
            if not stack:
                stack.append(i)
                continue
            if value>=heights[stack[-1]]:
                stack.append(i)
            else:
                while heights[stack[-1]]>value:
                    right=stack.pop()
                    maxarea=max(maxarea,heights[right]*(i-stack[-1]-1))
                stack.append(i)
        return maxarea


# @lc code=end

