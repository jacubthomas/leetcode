/*

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

Constraints:
0 <= rowIndex <= 33

*/
import java.util.List;
import java.util.ArrayList;
class Solution {
    public ArrayList<Integer> rowHelp(ArrayList<Integer> list, int rowIndex)
    {
        // build new set from row above
        ArrayList<Integer> newList = new ArrayList<Integer>();

        // open sandwich
        newList.add(1);
        if(rowIndex == 0)
            return newList;    
        
        // recursive call
        list = rowHelp(list, rowIndex-1);
        
        // fill middle
        for(int i=0; i<=list.size()-2; i++)
        {
            int left = list.get(i);
            int right = list.get(i+1);
            newList.add(left+right);
        }
        
        // close sandwich
        newList.add(1);
        return newList;
    }
    public List<Integer> getRow(int rowIndex) 
    {
        ArrayList<Integer> list = new ArrayList<Integer>();
        return rowHelp(list, rowIndex);
    }
}