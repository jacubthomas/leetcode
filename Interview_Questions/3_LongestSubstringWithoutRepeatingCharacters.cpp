#include <iostream>
#include <string>
#include <map>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
            
            //! Trivial cases
            if (s.length() < 2) return s.length();
    
            //! Two-Pointer approach
            int head = 0;
            int tail = 1;

            // ! Local & global counters tracking substring length
            int count = 0;
            int maxCount = 0;

            //! Key for determining character redundancy - all unique char in input
            map<char, bool> mapCharactersExplored;
            for (char character: s)
                mapCharactersExplored[character] = false;
    
            //! Setup problem
            resetSearch(mapCharactersExplored, count);

            //! Consider all all substrings
            while (head < s.length()-1) {

                //! Prevent tail from exceeding input s - reset and move on
                if (tail >= s.length())
                {
                    maxCount = max(maxCount, count);
                    resetSearch(mapCharactersExplored, count);
                    head++;
                    tail = head + 1;
                }
                //! Count first char of substring and mark as visited
                if (mapCharactersExplored[s[head]] == false) {
                    mapCharactersExplored[s[head]] = true;
                    count++;
                }
                //! Count tail character and mark as visited
                if (mapCharactersExplored[s[tail]] == false) {
                    mapCharactersExplored[s[tail]] = true;
                    tail++;
                    count++;
                    continue;
                }
                //! Tail character already visited - reset and move on
                if (mapCharactersExplored[s[tail]]) {
                    maxCount = max(maxCount, count);
                    resetSearch(mapCharactersExplored, count);
                    head++;
                    tail = head + 1;
                }
            }
            maxCount = max(maxCount, count);
            return maxCount;
        }
    
        //! Helper func - resetting character key and local count
        void resetSearch(map<char, bool> &mapCharactersExplored, int &count) {
            for (const auto& [key, value] : mapCharactersExplored) {
                mapCharactersExplored[key] = false;
            }
            count = 0;
        }
};


int main()
{
    Solution* s = new Solution();
    std::cout << "Max Count = " << s->lengthOfLongestSubstring(" ") << std::endl;
    std::cout << "Max Count = " << s->lengthOfLongestSubstring("AbcBa") << std::endl;
}

