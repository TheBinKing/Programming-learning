/*
 * @lc app=leetcode.cn id=1 lang=c
 *
 * [1] 两数之和
 * 在第一层for循环中选定一个元素，
 * 然后，在第二层for循环中遍历该元素之后的元素，
 * 看是否有和等于目标值的两个数。
 */

// @lc code=start


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int *returndata=malloc(2*sizeof(int));
    for(int i;i<numsSize;i++){
        for(int j=i+1;j<numsSize;j++){
            int all=nums[i]+nums[j];
            if(all==target){

                returndata[0]=i;
                /**/
                returndata[1]=j;
                *returnSize = 2;
                return returndata;
            }
        }
    }
    returndata[0]=0;
    /**/
    returndata[1]=0;
    *returnSize = 2;
    return returndata;
    return 2;
}
// @lc code=end

