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

    //! We pass down local sums to store the lower branch tilt calculations
    // We bubble back the path sum for the traversed branch to support higher branch tilt calculations
    int findTilt(TreeNode* root) {
        if (root == nullptr) return 0;
        //! We don't want to include tree's root, as it does not play a hand in tilt
        //! Thus, we handle some logic here and quick off helper down left & right branches
        int localSums = 0;
        int leftSum = helpCalculateTilt(root->left, localSums);
        int rightSum = helpCalculateTilt(root->right, localSums);
        return localSums + abs(leftSum - rightSum);
    }

    int helpCalculateTilt(TreeNode* root, int& localSums) {
        if (root == nullptr) return 0;

        int leftSum = helpCalculateTilt(root->left, localSums);
        int rightSum = helpCalculateTilt(root->right, localSums);

        localSums += abs(leftSum - rightSum);

        return leftSum + rightSum + root->val;
    }
};
