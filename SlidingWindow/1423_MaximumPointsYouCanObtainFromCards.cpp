class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int windowScore = 0;
        int maxScore = 0;
        int start = 0;
        int end = k-1;

        for (; start < k; start++) {
            windowScore += cardPoints[start];
        }
        maxScore = std::max(maxScore, windowScore);
        start = cardPoints.size() - 1;
        for (int i=0; i<k; i++) {
            windowScore -= cardPoints[end];
            end--;
            windowScore += cardPoints[start];
            start--;
            maxScore = std::max(maxScore, windowScore);
        }

        return maxScore;
    }
};
