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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        
        ListNode* l3 = new ListNode;
        ListNode* temp1 = list1;
        ListNode* temp2 = list2;
        ListNode* t3 = l3;

        while(temp1 != nullptr and temp2 != nullptr){
            if(temp1->val > temp2->val){
                
                t3->next = new ListNode(temp2->val);
                t3 = t3->next;
                temp2 = temp2->next;
            }
            else{
                t3->next = new ListNode(temp1->val);
                t3 = t3->next;
                temp1 = temp1->next;
            }
        }
        if(temp1 == nullptr){
            while(temp2 != nullptr){
                
                t3->next = new ListNode(temp2->val);
                t3 = t3->next;
                temp2 = temp2->next;
            }
        }
        else{
            while(temp1 != nullptr){
                t3->next = new ListNode(temp1->val);
                t3 = t3->next;
                temp1 = temp1->next;
            }
        }

        return l3->next;
    }
};