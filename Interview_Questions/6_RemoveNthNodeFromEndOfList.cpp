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
    //! Recursive helper, count node's traversed to get to tail
    int distanceToTail(ListNode* node) {
        if (node != nullptr && node->next == nullptr)
            return 0;
        return 1 + distanceToTail(node->next);
    }

    //! Recursive helper, find the node prior to target delete node
    ListNode* hopToNodePriorToDeleteNode(ListNode* node, int hopsRemaining) {
        if (!hopsRemaining) return node;
        return hopToNodePriorToDeleteNode(node->next, hopsRemaining-1);
    }

    ListNode* removeNthFromEnd(ListNode* head, int n) {
        //! Trivial case - one node in LinkedList
        if (head->next == nullptr) return nullptr;

        //! Locate the LinkedList's tail
        int hopsToTail = distanceToTail(head);

        //! Edge case - two node list, removing head
        if (hopsToTail < n) return head->next;

        //! Find the setup point, node before target delete node
        ListNode* priorNode = hopToNodePriorToDeleteNode(head, hopsToTail - n);
        //! Get the deleteNode
        ListNode* deleteNode = priorNode->next;
        //! Case where delete node points to another node 
        if (deleteNode->next != nullptr)
            priorNode->next = deleteNode->next;
        //! Case where delete node is the LinkedList tail
        else
            priorNode->next = nullptr;
        delete deleteNode;
        return head;
    }
};
