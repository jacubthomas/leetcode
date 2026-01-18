/*!
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    //! Use Fast-Slow pointer to detect cycle
    bool hasCycle(ListNode *head) {
        ListNode* nodeSlow = head;
        ListNode* nodeFast = head;
        while (nodeFast && nodeFast->next) {
            nodeSlow = nodeSlow->next;
            nodeFast = nodeFast->next->next;
            if (nodeSlow == nodeFast)
                return true;
        }
        return false;
    }
};
