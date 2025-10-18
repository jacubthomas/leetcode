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
    bool hasPathSumHelp(TreeNode* root, int targetSum, int count) 
    {
        if (root == nullptr) return false;
        else if (count + root->val == targetSum &&
                    root->left == nullptr &&
                    root->right == nullptr)
                    return true;

        bool left = hasPathSumHelp(root->left, targetSum, count + root->val);
        bool right = hasPathSumHelp(root->right, targetSum, count + root->val);
        
        return left || right;
    }

    bool hasPathSum(TreeNode* root, int targetSum) 
    {
        if (root == nullptr) return false;
        else if (root->val == targetSum && 
                root->left == nullptr &&
                root->right == nullptr)
            return true;

        return (
            hasPathSumHelp(root->left, targetSum, root->val) ||
            hasPathSumHelp(root->right, targetSum, root->val)
        );   
    }
};
