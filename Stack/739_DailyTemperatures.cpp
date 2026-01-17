#include <iostream>
#include <stack>
#include <vector>

using namespace std;

/*!
 * Here we leverage a monotonic stack
 * Every element above the other is an index that is monotonically increasing
 */
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> vecIntResult(temperatures.size(), 0);
        stack<int> stackIntTemps;
        //! Consider every day in temps
        for (int i = 0; i < temperatures.size(); i++) {
            int index = 0;
            if (stackIntTemps.empty() == false) {
                index = stackIntTemps.top();
            }
            while (stackIntTemps.empty() == false && //! Can't check if all prior days have already found their next warmer day
                   temperatures[i] > temperatures[index]) { //! Today is warmer than back then
                //! Update this result, we found days until next warmer day
                vecIntResult[index] = i - index;    //! We want days until warmer, not which day (which index)
                 //! This tempIndex is now accounted for, clear out
                stackIntTemps.pop();
                if (stackIntTemps.empty() == false) { //! Safety check
                    //! It's possible today is also warmer than the previous stack tempIndex as well
                    index = stackIntTemps.top();
                }
            }
            stackIntTemps.push(i); //! Consider every day, how many days until warmer than today
        }
        return vecIntResult;
    }
};

int main() {
    Solution s;
    vector<int> vecIntResult = s.dailyTemperatures({65, 70, 68, 60, 55, 75, 80, 74});
    for (int i=0; i < vecIntResult.size(); i++) { 
        cout << vecIntResult[i];
        if (i < vecIntResult.size()-1) cout << ", ";
    }
    cout << endl;
    return 0;
}
