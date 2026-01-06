class Solution {
public:
    /*!
     * Intuition - we don't need to modify any letters along the way
     * We look at the newest added letter, window[end]
     * We take the (WINDOW_SIZE - FREQUENCY_OF_NEW_LETTER_IN_WINDOW)
     * If that result is less than k, this is valid; otherwise, we need to shrink the window to abide k
     * Note that, once we begin expanding the window, we never need to shrink it all the way back down
     * It will only grow under valid circumstance - when this happens we will update our working result count
     */
    int characterReplacement(string s, int k) {
        map<int,int> mapState;          //! Counts of letters present in window
        int start = 0;                  //! Window Begin
        int maxLength = 0;              //! Working result
        int maxFreq = 0;                //! Secret sauce 
                                        //! largest frequency of identical (near) consecutive letter abiding k

        //! Consider the entire string, end when window edge reaches end of string
        for (int end=0; end < s.length(); end++) {
            mapState[s[end]] += 1;          //! Update letter count for the newest letter in window

            maxFreq = std::max(maxFreq, mapState[s[end]]);  //! Determine if the latest letter expands the window
            while ((end - start + 1) - maxFreq > k) {       //! Window too big, not abiding k - shrink it
                mapState[s[start]] -= 1;                    //! Shrink start letter count
                if (mapState[s[start]] == 0) {              //! Clean up letters no longer present in window
                    mapState.erase(s[start]);
                }
                start++;                                    //! Shrink window start towards end
            }

            maxLength = std::max(maxLength, end - start + 1); //! Update working result if window has grown
        }

        return maxLength;
    }
};
