/*
 * @lc app=leetcode.cn id=88 lang=c
 *
 * [88] 合并两个有序数组
 */

// @lc code=start


void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n){
    int l1=m-1;
    int l2=n-1;
    int tail=m+n-1;
    int temp;
    while(l1>=0||l2>=0){
        if(l1==-1){
            temp=nums2[l2--];
        }else if(l2==-1){
            temp=nums1[l1--];
        }else if(nums1[l1]>nums2[l2]){
            temp=nums1[l1--];
        }else{
            temp=nums2[l2--];
        }
        nums1[tail--]=temp;
    }
}
// @lc code=end

