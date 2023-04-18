#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:return 0
        m,n=len(matrix),len(matrix[0])
        # 记录当前位置上方连续“1”的个数
        pre=[0]*(n+1)
        res=0
        for i in range(m):
            for j in range(n):
                # 前缀和
                pre[j]=pre[j]+1 if matrix[i][j]=="1" else 0

            # 单调栈
            stack=[-1]
            for k,num in enumerate(pre):
                while stack and pre[stack[-1]]>num:
                    index=stack.pop()
                    res=max(res,pre[index]*(k-stack[-1]-1))
                stack.append(k)

        return res

    def largestRectangleArea(self,heights):
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
    def maximalRectangle0(self, matrix: List[List[str]]) -> int:
        maxarea=0
        tag=0
        for z in range(len(matrix)):
            height=[]
            for row in matrix:
                _temp=0
                for col in range(tag,len(row)):
                    if row[col]==1:
                        _temp+=1
                    else:
                        height.append(_temp)
                        break
            tag+=1       
            maxarea=max(maxarea,self.largestRectangleArea(height))
        return maxarea
            
# @lc code=end

