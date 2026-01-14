class Solution {
public:
    bool isValid(string s) {
        map<char,char> mapCloseToOpen;
        mapCloseToOpen[')'] = '(';
        mapCloseToOpen['}'] = '{';
        mapCloseToOpen[']'] = '[';
        stack<char> sOpenBrackets;
        
        for (int i=0; i < s.length(); i++) {
            if (mapCloseToOpen.find(s[i]) != mapCloseToOpen.end()) { //! closing bracket
                if (sOpenBrackets.empty() ||
                    sOpenBrackets.top() != mapCloseToOpen[s[i]]) // Mismatch
                    return false;
                else sOpenBrackets.pop(); //! Match - clear validated open bracket
            } 
            else //! opening bracket
                sOpenBrackets.push(s[i]);
        }

        return sOpenBrackets.size() == 0;
    }
};
