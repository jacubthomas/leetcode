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
    int longestUnivaluePath(TreeNode* root) {
        if (root == nullptr) return 0;

        int maxPath = 0;
        helpLongestUnivaluePath(root, maxPath);
        return maxPath;
    }

    int helpLongestUnivaluePath(TreeNode* node, int& maxPath) {
        if (node->left == nullptr && node->right == nullptr) //! Leaf node
            return 0;

        //! Trace left 
        int leftPath = 0;
        if (node->left != nullptr) {
            int leftRecurse = helpLongestUnivaluePath(node->left, maxPath) + 1;
            //! Only consider path if it matches current node
            if (node->left->val == node->val)
                leftPath += leftRecurse;
            //! Otherwise reset count
            else leftPath = 0;
        }
        // Trace right
        int rightPath = 0;
        if (node->right != nullptr) {
            int rightRecurse = helpLongestUnivaluePath(node->right, maxPath) + 1;
            //! Only consider path if it matches current node
            if (node->right->val == node->val)
                rightPath += rightRecurse;
            //! Otherwise reset count
            else rightPath = 0; 
        }

        //! Update max path observed
        maxPath = std::max (
            maxPath,
            leftPath + rightPath
        );

        //! Return longest univalue branch
        return std::max(leftPath, rightPath);
    }
};
