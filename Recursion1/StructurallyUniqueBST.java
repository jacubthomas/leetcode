/*

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes
of unique values from 1 to n. Return the answer in any order.

Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 8

*/
import java.util.List;
import java.util.ArrayList;
public class StructurallyUniqueBST 
{
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
    
    public class Solution 
    {
        // helper function
        public ArrayList<TreeNode> recurseTrees(int head, int tail)
        {
            // structure for return
            ArrayList <TreeNode> list = new ArrayList<TreeNode>();

            // base case
            if(head>tail)
            {
                list.add(null);
            }
            // loop over entire interval [1,n]
            for(int i=head; i<=tail; i++)
            {
                // break into halved subproblems
                ArrayList<TreeNode> left = recurseTrees(head, i-1);
                ArrayList<TreeNode> right = recurseTrees(i+1, tail);

                // assemble returned lists
                // each list will always be size 1, but none-null-nodes act as roots pointing towards nodes in subtrees
                for(TreeNode l : left)
                {
                    for(TreeNode r : right)
                    {
                        TreeNode root = new TreeNode(i, l, r);
                        list.add(root);
                    }
                } 
            }
            return list;
        }
        public List<TreeNode> generateTrees(int n) 
        {
            return recurseTrees(1,n);
        }
    }
}



