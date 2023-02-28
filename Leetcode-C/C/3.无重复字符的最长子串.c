/*
 * @lc app=leetcode.cn id=3 lang=c
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start


int lengthOfLongestSubstring(char * s){
    int count=0;  //the count num of char
    int max=0;   //max length
    int start=0;  //the current sting 
    int len=0;    //current len
    int temp[128]={0};  

    while(count<strlen(s)){
        if(temp[s[count]]>start){  //already appeaded   most important point
            len=count-start;
            max=(len>max)?len:max;
            start=temp[s[count]];  //refresh start
        }
        temp[s[count]]=count+1;
        count++;
    }
    len=count-start;
    return (len>max)?len:max;
}
// @lc code=end

