import java.util.ArrayList;

public class google1_simplified 
{
    public static int solution(Integer A[])
    {
        ArrayList<Integer> alist = new ArrayList<>();
        
        alist.add(A[1]);
        // int count = 1;
        for( int i = 1; i < A.length; i++ )
        {
            Boolean placed = false;
            for(int j=0; j < alist.size(); i++)
            {
                if(A[i].intValue() < alist.get(j).intValue())
                {
                    placed = true;
                    break;
                }
            }
            if( !placed )
                alist.add(A[i]);
        }
        return alist.size();
    }
    public static void main(String[] args) 
    {
        Integer[] A = new Integer[5];
        A[0] = 5;
        A[1] = 4;
        A[2] = 3;
        A[3] = 6;
        A[4] = 2;
        System.out.println(solution(A));
    }
}
