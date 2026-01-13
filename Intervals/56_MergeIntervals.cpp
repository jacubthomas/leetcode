class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        //! Trivial case
        if (intervals.size() < 2) return intervals;

        //! Let's sort by start time
        std::sort(intervals.begin(), intervals.end(), [](const vector<int>&a, const vector<int>&b) {
            return a[0] < b[0];
        });

        vector<vector<int>> vecSolutionIntervals = { intervals[0] };
        for (int i=1; i < intervals.size(); i++) {
            //! Overlapping case, next interval starts before our last ends
            //! Merge into one
            if (intervals[i][0] <= vecSolutionIntervals.back()[1])  {
                vecSolutionIntervals.back()[1] = std::max(intervals[i][1], vecSolutionIntervals.back()[1]);
            } 
            else //! No overlap, simply add to solution
                vecSolutionIntervals.push_back(intervals[i]);
        }

        return vecSolutionIntervals;
    }
};
