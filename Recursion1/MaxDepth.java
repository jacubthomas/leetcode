import java.util.HashMap;
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
        HashMap<Integer,Integer> memo;
        public int depthHelp(TreeNode node, int count)
        {
            if(node == null)
                return count - 1;
            
            // if(memo.containsKey(node.val))
            //     return memo.get(node.val);
            
            memo.putIfAbsent(node.val,
                Math.max(
                    depthHelp(node.left, count+1),
                    depthHelp(node.right, count+1)
                )
            );
            return memo.get(node.val);
        }
        public int maxDepth(TreeNode root) 
        {
            // <key = node.val,  value = max depth to leaf> 
            memo = new HashMap<Integer,Integer>();
            return depthHelp(root,1);
        }
    }
}
