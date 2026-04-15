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
    ListNode* sortList(ListNode* head) {
        vector<int> arr;
        ListNode* p1 = head;
        while(p1 != nullptr){
            arr.push_back(p1->val);
            p1 = p1->next;
        }
        sort(arr.begin(),arr.end());
        p1 = head;
        for(int x : arr){
            p1->val = x;
            p1 = p1->next;
        }
        return head;
    }
};