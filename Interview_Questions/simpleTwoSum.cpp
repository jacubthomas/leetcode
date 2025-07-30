#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> result = {-1, -1};
        for (int i=0; i < numbers.size()-1; i++)  {
            if (i > 0 && numbers[i-1] == numbers[i]) continue;
            for (int j=i+1; j < numbers.size(); j++) {
                const int tempResult = numbers[i] + numbers[j];
                if (tempResult == target) {
                    result[0] = i+1;
                    result[1] = j+1;
                    return result;
                }
            }
        }
        return result;
    }
};

int main() {
    Solution s;
    vector<int> vecIntInput = {-10,-8,-2,1,2,5,6};
    int target = 0;
    vector<int> result = s.twoSum(vecIntInput, target);
    cout << result[0] << ", " << result[1] << endl;
}
