
 // Definition for a binary tree node.
public class TreeNode 
{
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) 
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
class Solution {
    public TreeNode searchHelp(TreeNode node, int goal)
    {
        // base case 
        if(node == null)
            return null;
        
        // found! return rooted subtree
        if(node.val  == goal)
            return node;
        
        // traverse left & right branches
        TreeNode left = searchHelp(node.left, goal);
        TreeNode right = searchHelp(node.right, goal);
        
        return left != null ? left : right;
    }
    public TreeNode searchBST(TreeNode root, int val) 
    {
        return(searchHelp(root, val));
    }
}