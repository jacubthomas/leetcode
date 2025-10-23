/*!
Difficulty Medium 
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
 
Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
*/

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        //! Handle trivial case, only one interval
        if (intervals.size() == 1) return intervals;
        
        //! First we should sort intervals by interval starts
        std::sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        //! Make it easy on ourselves and write result to no data structure
        vector<vector<int>> result;

        //! Use two-pointers
        //! incrementing second when overlap
        //! incrementing first when no overlap
        for (int i=0; i < intervals.size(); i++) {
            if (i == intervals.size()-1) {
                result.push_back(intervals[i]);
                break;
            }
            for (int j=i+1; j < intervals.size(); j++) {
                if (intervals[i][1] >= intervals[j][0]) { //! Overlap detected - merge
                    if (intervals[i][1] < intervals[j][1])
                        intervals[i][1] = intervals[j][1];
                    if (j+1 == intervals.size()) {
                        result.push_back(intervals[i]);
                        i = j;  //! Move the first pointer to new interval start
                    }
                }
                else { //! Write merged result to return data structure
                    result.push_back(intervals[i]);
                    i = j-1;  //! Move the first pointer to new interval start
                    break;
                }
            }
        }

        return result;
    }
};
