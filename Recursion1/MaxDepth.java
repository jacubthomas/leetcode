public class MaxDepth 
{
    //  Definition for a binary tree node.
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
        public int depthHelp(TreeNode node, int count)
        {
            // non-existent branch
            if(node == null)
                return count - 1;
            
            // look left/right for longer path to bottom from node
            return Math.max(
                    depthHelp(node.left, count+1),
                    depthHelp(node.right, count+1)
                    );
        }
        public int maxDepth(TreeNode root) 
        {
            return depthHelp(root,1);
        }
    }
}
