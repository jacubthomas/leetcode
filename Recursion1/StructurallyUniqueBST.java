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
        public ArrayList<TreeNode> recurseTrees(int start, int end)
        {
            if(start > end || start < 1)
                return null;

            // generate list structure for return
            List<TreeNode> list = new ArrayList<TreeNode>();
            for(int i=start; start<=end; i++)
            {
                TreeNode node = new TreeNode(i);
                ArrayList<TreeNode> left = recurseTrees(i-1, start);
                ArrayList<TreeNode> right = recurseTrees(i+1, end);
                node.right = right.get(0);
                node.left = left.get(0);
                list.add(node);
            }
            return list;

        }
        public List<TreeNode> generateTrees(int n) 
        {
            return recurseTrees(1,n);
        }
    }
}


/*
if(n >= 1)
            {
                // update new chain
                TreeNode nu_node = new TreeNode(node.val);
                if(root.left == null && root.right == null)
                    root = nu_node;
                else if(root.left.val == node.val)
                    root.left = nu_node;
                else if(root.right.val == node.val) 
                    root.right = nu_node;   

                TreeNode left = new TreeNode(temp_stack.pop());
                nu_node.left = left;
                recurseTrees(list, n-1, left, root, temp_stack);

                if(root.val == nu_node.val)
                    root = node;
                
                // node.right = left;
                // node.left =  null;
                // recurseTrees(list, n-1, left, root, temp_stack);
                // temp_stack.push(left.val);
            }
            if(n > 1)
            {
                TreeNode left = new TreeNode(temp_stack.pop());
                node.left= left;
                TreeNode right = new TreeNode(temp_stack.pop());
                node.right= right;
                recurseTrees(list, n-2, left, root, temp_stack);
                recurseTrees(list, n-2, right, root, temp_stack);
            }
*/