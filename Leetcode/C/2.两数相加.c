/*
 * @lc app=leetcode.cn id=2 lang=c
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *head=NULL;
    struct ListNode *tail=NULL;
    int canary=0;
    while(l1||l2){
        int n1=l1?l1->val:0;
        int n2=l2?l2->val:0;
        int sum=(n1+n2+canary)%10;
        canary=(n1+n2+canary)/10;
        if(!head){
            head = tail = malloc(sizeof(struct ListNode));
            tail->val=sum;
            tail->next=NULL;
        }
        else{
            tail->next=malloc(sizeof(struct ListNode));;
            tail=tail->next;
            tail->val=sum;
            tail->next=NULL;
        }
        if(l1){        
            l1=l1->next;
        }
        if(l2){
            l2=l2->next;
        }
    }
    if(canary==1){
            tail->next=malloc(sizeof(struct ListNode));;
            tail=tail->next;
            tail->val=1;
            tail->next=NULL;
    }
    return head;
}
// @lc code=end

