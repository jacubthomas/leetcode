/*!
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
    //! Use Fast-Slow pointers to find middle node
    ListNode* middleNode(ListNode* head) {
        ListNode* nodeSlow = head;
        ListNode* nodeFast = head;
        while (nodeFast && nodeFast->next) {
            nodeSlow = nodeSlow->next;
            nodeFast = nodeFast->next->next;
        }
        return nodeSlow;
    }
};
