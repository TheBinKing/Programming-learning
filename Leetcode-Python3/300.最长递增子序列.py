#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start

memo_dic={}
def L_record(list,num):
    if num in memo_dic:
        return memo_dic[num]
    if num==len(list)-1:
        return 1
    max_len=1
    for i in range(num+1,len(list)):
        if list[i]>list[num]:
            max_len=max(max_len,L(list,i)+1)
    memo_dic[num]=max_len
    return max_len 
def L(list,num):
    if num==len(list)-1:
        return 1
    max_len=1
    for i in range(num+1,len(list)):
        if list[i]>list[num]:
            max_len=max(max_len,L(list,i)+1)
    return max_len  
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        L=[1]*n
        for i in reversed(range(n)):
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    L[i]=max(L[i],L[j]+1)
        return max(L)      
        
    def lengthOfLIS1(self, nums: List[int]) -> int:
        """
        增加了一个记事本，动态规划操作
        （直接提交testcase无法通过，但是调试可以通过testcase）
        """
        
        a= (L_record(nums,i) for i in range(len(nums)))
        return max(a)
        for i in a:
            print(i)
    

    def lengthOfLIS0(self, nums) -> int:
        """
        使用递归实现暴力枚举的方法，可以看作是动态规划前的一个预备路径
        """
        return max(L(nums,i) for i in range(len(nums)))
         
# @lc code=end

#a=Solution()
#nums = [7,7,7,7,7,7,7]
#a.lengthOfLIS(nums)