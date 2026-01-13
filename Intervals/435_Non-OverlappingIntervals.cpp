class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>> intervals) {
        //! Trivial case
        if (intervals.size() < 2) return 0;

        //! To find the optimal set of intervals, we need to consider their end times, not start
        std::sort(intervals.begin(), intervals.end(), [](const vector<int>&a , const vector<int>&b) {
            return a[1] < b[1];
        });

        //! Find the optimal set of non-overlapping intervals
        int countNonOverlappingIntervals = 1;
        vector<int> lastAddedInterval = intervals[0];
        for(int i=1; i < intervals.size(); i++) {
            if (intervals[i][0] >= lastAddedInterval[1]) {
                countNonOverlappingIntervals++;
                lastAddedInterval = intervals[i];
            }
        }

        //! (Total intervals) - (intervals in optimal solution) = min intervals to remove
        return intervals.size() - countNonOverlappingIntervals;
    }
};
