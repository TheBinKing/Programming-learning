#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if n==3: #只有三个数直接相加
            return nums[0]+nums[1]+nums[2]
        d=float('inf')
        nums=sorted(nums)
        ans=0
        for i in range(n):
            min,max=i+1,n-1
            while max>min:
                x=(nums[i]+nums[max]+nums[min])-target
                if abs(x)<d:
                    d=abs(x)
                    ans=nums[i]+nums[max]+nums[min]
                if x>0:
                    max-=1
                elif x<0:
                    min+=1
                else:
                    return target
        return ans
    def threeSumClosest0(self, nums: List[int], target: int) -> int:
        dic_=dict()
        for i in nums:
            distance=i-target
            if distance in dic_:
                dic_[distance]+=1
            else:
                dic_[distance]=1
        new_dic=sorted(dic_, key=lambda dict_key: abs(dic_[dict_key]))
        #keys=sorted(dic_.keys())
        num=0
        sum=0
        for key in new_dic:
            if new_dic[key]<=3:
                sum+=new_dic[key]*key
                num+=new_dic[key]
            else :
                return (key+target)*3
            if num==3:
                return sum+target*3
            

# @lc code=end

