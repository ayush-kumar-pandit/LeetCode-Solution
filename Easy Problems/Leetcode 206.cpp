/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head == nullptr) return head;
       
        ListNode* Ans = nullptr;

        ListNode* temp = Ans;

        while(head != nullptr){
            
            temp = new ListNode(head->val, Ans);
            head = head->next;
            Ans = temp;
        }
        return Ans;

    }
};