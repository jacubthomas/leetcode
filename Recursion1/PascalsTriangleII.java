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