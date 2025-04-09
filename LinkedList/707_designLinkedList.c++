/*
Difficulty Medium
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:
MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

Example 1:
Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:
0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
*/

struct Node {
public:
    int val;
    Node* next;
};

class MyLinkedList {
public:
    MyLinkedList() {
        m_head = nullptr;
    }
    
    int get(int index) {
        int i = 0;
        Node* node = m_head;
        while (node != nullptr && i < index) {
            node = node->next;
            i++;
        }
        return (node != nullptr) ? node->val : -1;
    }
    
    void addAtHead(int val) {
        Node* newNode = new Node();
        newNode->val = val;
        newNode->next = m_head;
        m_head = newNode;
    }
    
    void addAtTail(int val) {
        Node* newNode = new Node();
        newNode->val = val;
        newNode->next = nullptr;

        if (m_head == nullptr){
            m_head = newNode;
            return;
        }
        
        Node* traversalNode = m_head;
        while (traversalNode->next != nullptr) {
            traversalNode = traversalNode->next;
        }
        
        traversalNode->next = newNode;
    }
    
    void addAtIndex(int index, int val) {
        if (index == 0) {
            addAtHead(val);
            return;
        }
        
        Node* newNode = new Node();
        newNode->val = val;
        newNode->next = nullptr;
        
        int i = 0;
        Node* traversalNode = m_head;
        while (traversalNode != nullptr && i < index-1) {
            traversalNode = traversalNode->next;
            i++;
        }
        
        if (traversalNode != nullptr) {
            newNode->next = traversalNode->next;
            traversalNode->next = newNode;
        } else {
            delete newNode;
        }   
    }
    
    void deleteAtIndex(int index) {
        int i = 0;
        Node* node = m_head;
        if (node == nullptr) {
            return;
        }

        if (index == 0) {
            m_head = node->next;
            delete node;
            return;
        }
        
        i = 0;
        while (node != nullptr && i < index-1) {
            node = node->next;
            i++;
        }
        
        if (node != nullptr && node->next != nullptr) {
            Node* deleteNode = node->next;
            node->next = deleteNode->next;
            delete deleteNode;
        }
    }
    
    Node* m_head;
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
