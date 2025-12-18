class Solution {
public:

    void calculateWaterTrappedInOneRegion(vector<int>& height, int& left, int& right, int& sumWaterTrapped) {
        if (right == height.size()) right--;
        const int minWallHeight = min(height[left], height[right]); //! Water can't overflow trap edge
        left++; // Step in to the actual blocks where water may be trapped
        while (left < right) {
            //! Water trapped here, add it to sum
            if (height[left] < minWallHeight) sumWaterTrapped += minWallHeight - height[left];
            left++; //! Step on
        }
    }

/*! CAN ASSUME IN THIS CASE THAT INITIAL HEIGHT[LEFT] IS TALLER THAN EVERYTHING ELSE
 * CAN NOT ASSUME RIGHT IS THE TRUSTED HEIGHT FOR WATER TRAPPING
 * WE ALSO CAN NOT ASSUME THESE CONDITIONS AREN'T ACTUALLY CORRECT.... I.E. 4 2 3
 *
 * BUT WE KNOW THIS IS THE LAST CHUNK, AND OUR ORIGINAL ALGO DO THE WORK IF WE FEED IT THE REVERSED FINAL CHUNK 
*/
    void calculateWaterTrappedInFinalRegion(vector<int>& height, int& left, int& right, int& sumWaterTrapped) {
        std::vector<int> subset(height.begin() + left,
                                height.end());
        std::reverse(subset.begin(), subset.end());
        right = height.size()+1;
        sumWaterTrapped += trap(subset);
    }

    int trap(vector<int>& height) {
        int sumWaterTrapped = 0;
        int i = 0;
        for (int i=0; i < height.size()-1; i++) {
            int left = i;
            int right = i+1;
            while (right < height.size()) { //! Stay in bounds
                //! Case 1: We reach edge of water trap
                if (height[right] >= height[left]) {
                    calculateWaterTrappedInOneRegion(height, left, right, sumWaterTrapped);
                    break;
                }
                // Case 2: We are potentially collecting water, keep growing right for more
                else
                    right++;
            }
            
            //! We are at the end of the line
            if (right >= height.size()) {
                //! Final edge case, where right height never measures up to left height
                if (left != right)
                    calculateWaterTrappedInFinalRegion(height, left, right, sumWaterTrapped);
                if (right >= height.size())
                    break;
            }
            //! We are NOT at the end of the line
            //! We've just calculated one water pocket
            else i = right-1;
        }
        
        return sumWaterTrapped;
    }
};


/*

    Thought process in solving this conceptually before coding
    X = Height blocks
    O = Water trapped

    Case 1: where it's plain to see that with left = 0 and right = 2,
    there is no point in continuing to move right. Just sum this and move on

        
        X  
    X O X X
    X X X X
    0 1 2 3
    L   R
    L     R
    L     

    So we establish a rule, if h[right] >= h[left], add the area trapped to sum & move on
    Like such:
        
        X  
    X O X X
    X X X X
    0 1 2 3
    L   R
        L R

    So how do we sum, because it's not going to be perfectly rectangular area...


                        X O O X
        X               X O X X
    X O X               X O X X
    X X X               X X X X
    0 1 2               0 1 2 3

    We get 1            We get 4

    - We note the note minimum of the edge heights, minWallHeight = min(h[left], h[right])
    - And we takes steps
        - left++
    - After each step we ask, did we hit the right edge
        - if not, we ask, is h[left] < minWallHeight
            - if so, localSum += minWallHeight - h[left]

    -------------------------------------------------------------------------------------

    This leads to an implied second rule:
    If h[left] > h[right], keep incrementing right until the above is true

    Case 2.1 where it's plain to see that we keep moving R until the above

    X O O X
    X X O X
    X X X X
    0 1 2 3
    L R
    L   R
    L     R

    -------------------------------------------------------------------------------------
    However, edge case? say towards the end, maybe h[right] never again exceeds h[left]...
    But maybe there is a pocket of water if we increment left

    Case 2.2: where h[left] > [right], but it actually makes sense to move left
    
    X    
    X X O X
    X X X X
    0 1 2 3
    L R
    L   R
    L     R
      L   R

-------------------------------------------------------------------------------------------

How we handle the last two cases above depends on how calculate area
Let's look at the actual area of water, water being O

    X                   X O O X
    X X O X             X X O X
    X X X X             X X X X
    0 1 2 3             0 1 2 3

    We get 1            We get 3

Eureka moment?
To case 2.1 & 2.2, we will take different strategies, dependent on does h[left] == h[right]

if h[left] == h[right]
   - We take steps until left reaches right
   - On each step, calculate local area sum by doing 
        - left++
        - localSum += h[left-1] - h[left]
else
   - We take steps until left reaches right
   - On each step, we ask, is h[left] < h[right]
        - if so:
            - localSum += h[right] - h[left]
        - Then no matter what, we take step:
            - left++


 X              
 X   X           X
 X X X           X X   X 
 X X X           X X X X X
 0 1 2           0 1 2 3 4
 4 3 2           3 2 1 2 1

     X
 X   X                   X
 X X X             X   X X 
 X X X           X X X X X
 

 X
 X X
 X X
 X X O X
 X X X X
 0 1 2 3




*/
