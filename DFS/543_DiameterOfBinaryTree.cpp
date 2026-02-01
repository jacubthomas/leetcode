/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
     if (root == nullptr) return 0;
        
        int maxPath = 0;
        helpMaxDiameter(root, maxPath);

        return maxPath;
    }
    
    int helpMaxDiameter(TreeNode* node, int& maxPath) {
        if (node->left == nullptr && node->right == nullptr) return 0;

        int leftPathLength = 0;
        if (node->left != nullptr) 
            leftPathLength = helpMaxDiameter(node->left, maxPath) + 1;
        int rightPathLength = 0;
        if (node->right != nullptr) 
            rightPathLength = helpMaxDiameter(node->right, maxPath) + 1;

        int fullPath = leftPathLength + rightPathLength;
        maxPath = max(maxPath, fullPath);

        return max(leftPathLength, rightPathLength);
    }
};
