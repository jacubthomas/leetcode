#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

class Solution {
public:

    static bool comp(int a, int b) {
        return a < b;
    }

    void recurseCombinations(vector<int>& candidates, 
                            set<vector<int>>& resultSets,
                            int numOnes,
                            int tempTarget,
                            vector<int> subResultSet,
                            int minIndex) {
        if (tempTarget == 0) {
            resultSets.insert(subResultSet);
            return;
        }

        if (tempTarget <= numOnes) {
            std::vector<int> result;
            for (int i=0; i < tempTarget; i++)
                result.push_back(1);
            for (int num : subResultSet)
                result.push_back(num);
            resultSets.insert(result);
        }

        for (int i=minIndex; i < candidates.size(); i++) {
            if (tempTarget >= candidates[i] ){
                subResultSet.push_back(candidates[i]);
                recurseCombinations(candidates,
                                    resultSets,
                                    numOnes,
                                    tempTarget - candidates[i],
                                    subResultSet,
                                    i+1);
                subResultSet.pop_back();
            } else return;
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        
        set<vector<int>> resultSets;

        //! Order should only help, sort ascending
        sort(candidates.begin(), candidates.end(), comp);

        //! 1's can scale out the problems recursion stack - we'll handle the specially
        int numOnes = 0;
        for (int i=0; i < candidates.size(); i++) {
            if (candidates[i] == 1) numOnes++;
            else break;
        }
        if (numOnes >= target) {
            vector<int> onesVector;
            for (int i=0; i < target; i++)
                onesVector.push_back(1);
            resultSets.insert(onesVector);
        }

        for (int i=numOnes; i < candidates.size(); i++) {
            if (candidates[i] <= target) {
                recurseCombinations(candidates, 
                                    resultSets,
                                    numOnes, 
                                    target - candidates[i],
                                    {candidates[i]},
                                    i+1);
            } else break;
        }
        vector<vector<int>> resultVector(resultSets.begin(), resultSets.end());
        return resultVector;
    }

};

int main() {
    Solution s;
    vector<int> candidates = {10,1,2,7,6,1,5};
    int target = 8;
    // candidates = {2,5,2,1,2};
    // target = 5;
    // candidates = {1,1,1,1,1,
    //                 1,1,1,1,1,
    //                 1,1,1,1,1,
    //                 1,1,1,1,1,
    //                 1,1,1,1,1,1,1};
    // target = 27;
    // candidates = {4,1,1,4,4,4,4,2,3,5};
    // target = 10;
    vector<vector<int>> results = s.combinationSum2(candidates, target);
    cout << "Results { ";
    for (vector<int> innerVec : results) {
        cout << " { ";
        for (int num : innerVec) {
            cout << num << " ";
        }
        cout << "}, ";
    }
    cout << " } " << endl;
}
