class Solution {
public:
    bool anagramFound(map<char,int>& mapCurrentState, map<char,int>& mapProvidedAnagramState){
        if (mapCurrentState.size() != mapProvidedAnagramState.size()) return false;

        for (auto it = mapCurrentState.begin(); it != mapCurrentState.end(); ++it) {
            //! Found a letter not present in the anagram, invalid
            if (mapProvidedAnagramState.find(it->first) == mapProvidedAnagramState.end())
                return false;
            //! Letter counts don't match up, invalid
            if (mapProvidedAnagramState[it->first] != it->second)
                return false;
        }
        
        return true;
    }

    //! Fixed window
    vector<int> findAnagrams(string s, string p) {
        vector<int> vecSolutionIndices;         //! Return Value

        //! Trivial case
        if (s.length() == 1) {
            if (s.compare(p) == 0) // 0 is equal!
                vecSolutionIndices.push_back(0);
            return vecSolutionIndices;
        } 

        map<char,int> mapWindowState;           //! State of current search window

        //! Gather the letter counts of the provided anagram for comparison
        map<char,int> mapProvidedAnagramState;  //! State of the anagram, letter counts
        for (char c: p)
            mapProvidedAnagramState[c]++;

        int right = 0;
        const int fixedWindowSize = p.length();
        for (int left = 0; right < s.size(); right++) {
            mapWindowState[s[right]]++;                     //! Always add next character to state
            const int windowSize = right - left + 1;        //! For readability's sake
            if (windowSize == fixedWindowSize) {            //! Potential anagram
                if (anagramFound(mapWindowState, mapProvidedAnagramState))  // evaluate
                    vecSolutionIndices.push_back(left);     //! Found one! Update solution vector
                mapWindowState[s[left]]--;                  //! Decrement one letter count as we slide
                if (mapWindowState[s[left]] == 0) mapWindowState.erase(s[left]); //! Keep state map trim
                left++;                                     //! Window is correct size, now slide along
            }
        }
        
        return vecSolutionIndices;
    }
};
