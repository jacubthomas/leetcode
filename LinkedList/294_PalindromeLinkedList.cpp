class Solution {
public:

    const bool hasOddNumberOfNodes(ListNode* head) {
        int count = 1;
        while (head->next != nullptr) {
            head = head->next;
            count++;
        }
        return count % 2 == 1;
    }

    //! Fast-Slow pointer to identify and return middle node of LL
    ListNode* getMiddleNode(ListNode* head) {
        ListNode* nodeSlow = head;
        ListNode* nodeFast = head;
        //! Node fast will move 2x node slow
        //! When node fast reaches end, node slow will only be halfway
        while (nodeFast != nullptr && nodeFast->next != nullptr) {
            nodeSlow = nodeSlow->next;
            nodeFast = nodeFast->next->next;
        }
        return nodeSlow;
    }

    bool isPalindrome(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return true;
        if (head->next->next == nullptr) return head->val == head->next->val;

        //! Determine if list has odd or even number of nodes
        const bool oddNumberOfNodes = hasOddNumberOfNodes(head);

        //! Identify the middle node - consider odd/even case
        ListNode* middleNode = getMiddleNode(head);

        stack<int> stackVals;
        if (oddNumberOfNodes) {
            while (head != middleNode) { 
                stackVals.push(head->val);
                head = head->next;
            }
            head = head->next; //! Skip middle node

            while(stackVals.empty() == false) {
                if (stackVals.top() != head->val) return false;
                stackVals.pop();
                head = head->next;
            }
        } else {
            while (head != middleNode) { 
                stackVals.push(head->val);
                head = head->next;
            }
            while(stackVals.empty() == false) {
                if (stackVals.top() != head->val) return false;
                stackVals.pop();
                head = head->next;
            }
        }
        return true;
    }
};
