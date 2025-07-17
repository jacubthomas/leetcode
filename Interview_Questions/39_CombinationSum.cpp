/*
 * Difficulty Medium
 * 
 * Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates
 * where the chosen numbers sum to target. You may return the combinations in any order. The same number may be chosen from candidates
 * an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different. The
 * test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the 
 * given input.
 * 
 * Example 1:
 * Input: candidates = [2,3,6,7], target = 7
 * Output: [[2,2,3],[7]]
 * Explanation:
 * 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
 * 7 is a candidate, and 7 = 7.
 * These are the only two combinations.
 * 
 * Example 2:
 * Input: candidates = [2,3,5], target = 8
 * Output: [[2,2,2,2],[2,3,3],[3,5]]
 * 
 * Example 3:
 * Input: candidates = [2], target = 1
 * Output: []
 * 
 * Constraints:
 * 1 <= candidates.length <= 30
 * 2 <= candidates[i] <= 40
 * All elements of candidates are distinct.
 * 1 <= target <= 40
 */

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    static bool comp(int a, int b) {
        return a < b;
    }

    void recursePermutations(vector<int>& candidates, int tempTarget, int minCandidate, vector<int> subResultSet) {
        //! Trivial case where candidate is the target
        if (tempTarget == 0) {
            m_resultSets.push_back(subResultSet);
            return;
        }
        //! Consider permutations of each candidate from minCandidate up
        for (int i=minCandidate; i < candidates.size(); i++) {
            //! We have found a new result set summing to target
            if (tempTarget - candidates[i] == 0) {
                subResultSet.push_back(candidates[i]);
                m_resultSets.push_back(subResultSet);
                return;
            }
            //! We have a potential new result set forming
            else if (tempTarget - candidates[i] > 0) {
                subResultSet.push_back(candidates[i]);
                recursePermutations(candidates, tempTarget - candidates[i], i, subResultSet);
                subResultSet.pop_back(); //! put it back as it where for other candidates to be attached to this subset
            }
            else break; //! Ascending order so nothing after will work - stop short
        }

    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {

        //! Sort candidate ints in ascending order
        sort(candidates.begin(), candidates.end(), comp);

        //! Consider all candidates, recursively seek out all permutations of acceptable result sets
        for (int i=0; i < candidates.size(); i++) {
            if (candidates[i] <= target)
                recursePermutations(candidates, target - candidates[i], i, {candidates[i]});
            else break; //! Don't bother with candidates bigger than the target, we can stop early here
        }
        
        return m_resultSets;
    }

    vector<vector<int>> m_resultSets;
};

int main() {
    Solution s;
    vector<int> candidates = {2,3,5};
    int target = 8;
    candidates = {2,3,6,7};
    target = 7;
    vector<vector<int>> results = s.combinationSum(candidates, target);
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
