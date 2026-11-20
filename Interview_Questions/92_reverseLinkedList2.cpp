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
 // before, current, after
class Solution {
public:

    //! Pointers need to be passed via reference for these changes to persist
    void reverseNode(ListNode*& previous,
                        ListNode*& current,
                        ListNode*& next)
    {
        current->next = previous;
        previous = current;
        current = next;
        if (next) 
            next = next->next;
    }

    void advanceNodes(ListNode*& previous,
                        ListNode*& current,
                        ListNode*& next)
    {
        previous = current;
        current = next;
        if (next) 
            next = next->next;
    }

    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || !head->next) return head;

        ListNode* previous = nullptr;
        ListNode* current = head;
        ListNode* next = head->next;
        ListNode* newStartNode = nullptr;
        ListNode* newEndNode = nullptr;
        int i = 1;
        while (current)
        {
            if (i < left)
            {
                if (i == left - 1) newStartNode = current;
                advanceNodes(previous, current, next);
            }
            else if (i > right) 
                break;
            else
            {
                if (i == left) newEndNode = current;
                else if (i == right)
                {
                    if (newStartNode) newStartNode->next = current;
                    else head = current;
                }
                reverseNode(previous, current, next);
            }
            i++;
        }
        if (newEndNode) 
            newEndNode->next = current;
        return head;
    }
};
