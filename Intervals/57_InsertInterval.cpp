class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        // trivial case
        if (intervals.size() == 0) {
            intervals.push_back(newInterval);
            return intervals;
        }

        //! let's make it easy on ourselves
        //! push our newInterval onto list, sort, and run simple merge
        intervals.push_back(newInterval);

        //! Sort by Start time
        std::sort(intervals.begin(), intervals.end(), [] (const vector<int>&a, const vector<int>& b) { 
            return a[0] < b[0];
            });

        //! Now run simple merge
        vector<vector<int>> resultIntervals = {intervals[0]};
        for (int i=1; i<intervals.size(); i++) {
            // currentInterval starts at or before lastInterval ends - merge
            if (intervals[i][0] <= resultIntervals.back()[1]) {
                resultIntervals.back()[1] = std::max(intervals[i][1], resultIntervals.back()[1]);
            //! currentInterval is not overlapping with previous
            } else {
                resultIntervals.push_back(intervals[i]);
            }
        }
        return resultIntervals;
    }
};
