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

    /////////////////////
    /// Solution 1
    /////////////////////
    int distanceToTail(ListNode* node) {
        if (node != nullptr && node->next == nullptr)
            return 0;

        return 1 + distanceToTail(node->next);
    }

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

        //! Find the setup point, node before target
        ListNode* priorNode = hopToNodePriorToDeleteNode(head, hopsToTail - n);
        ListNode* deleteNode = priorNode->next;
        if (deleteNode != nullptr) { 
            if (deleteNode->next != nullptr)
                priorNode->next = deleteNode->next;
            else
                priorNode->next = nullptr;
            delete deleteNode;
        }
        return head;
    }

    /////////////////////
    /// Solution 2
    /////////////////////
    //! Gather list length by traversing it entire
    int determineListLength(ListNode* head) {
        int listLength = 0;
        ListNode* node = head;
        while (node != nullptr) {
            listLength++;
            node = node->next;
        }
        return listLength;
    }

    ListNode* removeNthFromEnd(ListNode* head, int n) 
    {
        //! Trivial cases
        if (head == nullptr) return nullptr;
        else if (head->next == nullptr) {
            if (n >= 1) return nullptr;
            else return head;
        }

        const int listLength = determineListLength(head);

        if (n == listLength) { //! Off with the head
            head = head->next;
        } else { //! Somewhere down chain
            ListNode* prevNode = head;
            int stepsToPrevNode = listLength - n - 1;
            while (stepsToPrevNode > 0) {
                prevNode = prevNode->next;
                stepsToPrevNode--;
            }

            ListNode* removeNode = prevNode->next;

            //! Consider if removeNode is tail
            if (removeNode->next == nullptr) {
                prevNode->next = nullptr;
                delete removeNode;
            } else {
                ListNode* nextNode = removeNode->next;
                prevNode->next = nextNode;
                delete removeNode;
            }
        }
        return head;
    }
};
