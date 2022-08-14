import java.util.ArrayList;
import java.util.Collections;

public class ArraytoAL 
{
    public static void main(String[] args) 
    {
        Integer[] A = new Integer[5];
        ArrayList<Integer> al = new ArrayList<>();
        for(int i = 1; i < 5; i++)
        {
            A[i] =  ((i + 5) * 30) % 23;
            System.out.println(A[i]);
            al.add(A[i]);
        }
        // List<Integer> l = Arrays.asList(A);
        Collections.sort(al, Collections.reverseOrder());
        while  ( !al.isEmpty() )
        {
            Integer temp = al.get(0);
            al.remove(0);
            System.out.println(temp.toString());
        }
    }
}


/*
// public static void main(String[] args) 
    //   {
    //     // // Read from stdin, solve the problem, write answer to stdout.
    //     // Scanner in = new Scanner(System.in);
    //     // Integer[] A = getIntegerArray(in.next());
    //     Integer[] A = new Integer[5];
        
    //     for(int i = 0; i < 5; i++)
    //     {
    //         A[i] =  i + 5;
    //         System.out.println(A[i]);
    //     }


    //     // System.out.print(solution(A));
    //   }
    */