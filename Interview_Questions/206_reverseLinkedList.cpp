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

    ListNode* reverseList(ListNode* head) 
    {
        if (!head || !head->next) return head;

        ListNode* previous = nullptr;
        ListNode* current = head;
        ListNode* next = head->next;
        while (current)
        {
           reverseNode(previous, current, next);
        }
        return previous;
    }
};
