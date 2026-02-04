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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> vecResult;
        if (root == nullptr) return vecResult;

        queue<TreeNode*> q;
        q.push(root);

        while (q.empty() == false) {
            const int levelSize = q.size();
            int rightMostValInLevel;
            for (int i=0; i < levelSize; i++) {
                TreeNode* node = q.front();
                q.pop();
                rightMostValInLevel = node->val;
                if (node->left != nullptr) q.push(node->left);
                if (node->right != nullptr) q.push(node->right);
            }
            vecResult.push_back(rightMostValInLevel);
        }

        return vecResult;
    }
};
