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
     vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<int> vecCurrentPath;
        vector<vector<int>> vecVecSolutionPaths;
        pathSumHelp(root, targetSum, 0, vecCurrentPath, vecVecSolutionPaths);
        return vecVecSolutionPaths;
    }
    //! Additional params attached to helper:
    //! @Param - 3rd current path sum
    //! @Param - 4rd list nodes along current paths
    //! @Param - 5th list of all solution paths
    //! @Return - void, list of solution paths size is our answer
    void pathSumHelp(TreeNode* root, 
                    const int target,
                    int sum,
                    vector<int>& vecCurrentPath,
                    vector<vector<int>>& vecVecSolutionPaths) {
        //! Base case
        if (root == nullptr)
            return;

        //! Add current node to the mix
        sum += root->val;
        vecCurrentPath.push_back(root->val);

        //! Go left & right
        pathSumHelp(root->left, target, sum, vecCurrentPath, vecVecSolutionPaths);
        pathSumHelp(root->right, target, sum, vecCurrentPath, vecVecSolutionPaths);

        if (root->left == nullptr && root->right == nullptr && //! Node is a leaf
            sum == target)                                     // Path sums to target
            vecVecSolutionPaths.push_back(vector<int>(vecCurrentPath)); //! Push a copy
        
        //! Undo node from current path, since we pass by reference
        vecCurrentPath.pop_back();
     }
    
};
