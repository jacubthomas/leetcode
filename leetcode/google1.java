package src.leetcode;
/*
You are given an array A representing heights of students. All the students are asked to stand in rows. The students arrive by one, sequentially (as their heights appear in A). For the i-th student, if there is a row in which all the students are taller than A[i], the student will stand in one of such rows. If there is no such row, the student will create a new row. Your task is to find the minimum number of rows created.

Write a function that, given a non-empty array A containing N integers, denoting the heights of the students, returns the minimum number of rows created.

For example, given A = [5, 4, 3, 6, 1], the function should return 2.

Students will arrive in sequential order from A[0] to A[N−1]. So, the first student will have height = 5, the second student will have height = 4, and so on.

For the first student, there is no row, so the student will create a new row.

Row1 = [5]

For the second student, all the students in Row1 have height greater than 4. So, the student will stand in Row1.

Row1 = [5, 4]

Similarly, for the third student, all the students in Row1 have height greater than 3. So, the student will stand in Row1.

Row1 = [5, 4, 3]

For the fourth student, there is no row in which all the students have height greater than 6. So, the student will create a new row.

Row1 = [5, 4, 3]

Row2 = [6]

For the fifth student, all the students in Row1 and Row2 have height greater than 1. So, the student can stand in either of the two rows.

Row1 = [5, 4, 3, 1]

Row2 = [6]

Since two rows are created, the function should return 2.

Assume that:

N is an integer within the range [1..1,000]

each element of array A is an integer within the range [1..10,000]

In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment
*/

import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.stream.Stream;

public class google1
{   
    class Solution {
    
      static int solution(Integer[] A) 
      {
                // Your solution goes here.
                ArrayList<PriorityQueue> a_pq = new ArrayList();
                PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
                ArrayList<Integer> al = new ArrayList();
                for ( Integer x : A )
                    al.add(x);
        
                pq.add(al.get(0));
                a_pq.add(pq);
               // for all values in og list
               for (int i=1; i < al.size(); i++)
               {
                Boolean placed = false;
                // for all priority queues
                for( int j = 0; j < a_pq.size(); j++)
                {
    
                    PriorityQueue<Integer> temp = a_pq.get(j);
                  //System.err.println(al.get(i) + " <  " + temp.peek().intValue());
                    if ( al.get(i).intValue() < temp.peek().intValue())
                    {
                        pq.add(al.get(i));
                        placed = true;
                        break;
                    }
                }
                    if( !placed )
                    {
                        PriorityQueue<Integer> pq2 = new PriorityQueue<Integer>();
                        pq2.add(al.get(i));
                        a_pq.add(pq2);
                    }
               }
              return a_pq.size();
      }
    
      public static void main(String[] args) 
      {
        // Read from stdin, solve the problem, write answer to stdout.
        Scanner in = new Scanner(System.in);
        Integer[] A = getIntegerArray(in.next());
    
        System.out.print(solution(A));
      }
    
      private static Integer[] getIntegerArray(String str) 
      {
        return Stream.of(str.split("\\,"))
              .map(Integer::valueOf)
              .toArray(Integer[]::new);
      }
    }
}
class SortByHeight implements Comparator<Integer>
    {
        public int compare(Integer a, Integer b)
        {
            if ( a < b )
                return 1;
            else if ( a > b )
                return -1;
            else
                return 0;
        }
    }