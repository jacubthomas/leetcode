#include <queue>
#include <utility>
#include <vector>

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        //! Sort intervals by start time, ascending
        std::sort(intervals.begin(), intervals.end(), [] (const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        //! Comparator for heap - min heap by end time
        auto comp = [](const int& a, const int& b) {
            return a > b; //! Greater IS min heap
        };

        //! Establish a min heap, push meeting end times onto
        priority_queue<int, vector<int>, decltype(comp)> pqMeetingEnds(comp);
        
        int iMaxMeetingRooms = 0;
        //! Consider all intervals
        for (vector<int> meeting: intervals) {
            //! First we pop any meetings that have wrapped
            while (pqMeetingEnds.empty() == false &&
                    pqMeetingEnds.top() <= meeting[0])
                    pqMeetingEnds.pop();
            //! Then we add this new meeting which is just starting
            pqMeetingEnds.push(meeting[1]);
            //! Last we check how many meetings are going on simultaneously - update max accordingly
            iMaxMeetingRooms = std::max(iMaxMeetingRooms, (int)pqMeetingEnds.size());
        }
        return iMaxMeetingRooms;
    }
};
