class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        //! Trivial Cases
        if (piles.size() == 0) return 0;
        if (piles.size() == 1) piles[0];

        // Find pile with the largest count
        int maxPiles = 0;
        for (int pile: piles) {
            maxPiles = max(maxPiles, pile);
        }

        //! Search space of rates per hour is [1,h]
        int left = 1;
        int right = maxPiles;
        //! Any rate should be slower than this
        int slowestRatePerHour = std::numeric_limits<int>::max();
        // Keep shrinking until our window is completely closed
        while (left <= right) {
            //! Left + middle_window_offset
            int mid = left + ((right - left) / 2);
            int sumHours = 0;
            for (int pile: piles) {
                // Discrete numbers only, round up
                int quotient = pile / mid;
                if (pile % mid > 0) quotient++;
                sumHours += quotient;
                //! Short-circuit if we're already above max hours
                if (sumHours > h) break;
            }
            //! Narrow the search
            if (sumHours <= h) { //! Valid case - within the alloted time
                if (mid < slowestRatePerHour) slowestRatePerHour = mid;
                right = mid - 1;
            } else //! Invalid case - over the alloted time
                left = mid + 1;
        }
        return slowestRatePerHour;
    }
};
