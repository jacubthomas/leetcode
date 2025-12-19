/*!
Medium
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
*/

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
    ListNode* rotateRight(ListNode* head, int k) {
        //! Trivial Case #1
        if (head == nullptr) return head;
        // int left;
        // int right;
        int linkedListLength = 0;

        //! Sus out the length of the list
        ListNode* node = head;
        while (node != nullptr) {
            linkedListLength++;
            node = node->next;
        }

        //! Trivial Case #2
        if (linkedListLength == 1) return head;

        //! Trivial Case #3
        if (linkedListLength == 2) {
            if (k % 2 == 1) {
                head->next->next = head;
                head = head->next;
                head->next->next = nullptr;
            }
            return head;
        }

        //! Eliminate all the rollover work
        //! Just work within the final remaining rotations
        if (k >= linkedListLength) {
            k = k % linkedListLength;
        } 

        //! Trivial Case #3
        if (k == 0) return head;
        
        //! Align left pointer one node left of final head node
        int kFromTail = linkedListLength;
        ListNode* leftNode = head;
        while (kFromTail > k+1) {
            leftNode = leftNode->next;
            kFromTail--;
        }

        while (k != 0) {
            ListNode* right = leftNode;
            //! Align right one node left of current tail
            while(right->next->next != nullptr) {
                right = right->next;
            }
            //! Rotate tail into head
            right->next->next = head;
            head = right->next;
            right->next = nullptr;
            k--;
        }
        return head;
    }
};
