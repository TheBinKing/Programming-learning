#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """_summary_
        大容器的存放方法
        1.通过遍历扫描全过程进行标注，对于出现在区间内的值标记为1，否则为0，如果遇到单个元素的区间进进行额外的标记（2），同时遍历过程中记录下整体上下区间的范围
        2.第二次在容器中进行遍历，寻找10的边界，遇到之后登记有效区间。
        3.如果遇到单元素特殊标记则需要判断其前面的状态是否满足合并的条件如果满足则并入前面的区间
        
        
        170/170 cases passed (64 ms)
        Your runtime beats 16.77 % of python3 submissions
        Your memory usage beats 5.11 % of python3 submissions (19.3 MB)
        Args:
            intervals (List[List[int]]): _description_

        Returns:
            List[List[int]]: _description_
        """
        max=-1
        min=10000
        record=[0]*10001
        special=0
        for qujian in intervals:
            if qujian[0]==qujian[1]:
                record[qujian[0]]=2
        for qujian in intervals:
            if qujian[1]>max:
                max=qujian[1]
            if qujian[0]<min:
                min=qujian[0]
            for i in range(qujian[0],qujian[1]):
                record[i]=1

        left,right=-1,-1
        qujian_temp=[0,0]
        all_qujian=[]
        for i in range(min,max+1):
            if record[i]==1 and left==-1:
                left=i
            if record[i-1]==1 and record[i]==0 and left!=-1:
                right=i
                qujian_temp=[left,right]
                all_qujian.append(qujian_temp)
                left,right=-1,-1
            if record[i]==2:
                if record[i-1]==1:
                    right=i
                    qujian_temp=[left,right]
                    all_qujian.append(qujian_temp)
                    left,right=-1,-1
                if record[i-1]!=1:
                    all_qujian.append([i,i])
                    #left =i+1

        return all_qujian



# @lc code=end


