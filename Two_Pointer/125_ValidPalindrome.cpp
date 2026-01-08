class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0; 
        int right = s.length() - 1;
        std::transform(s.begin(), s.end(), s.begin(), [](unsigned char c) { return std::tolower(c);});
        while (left < right) {
            if (std::isalnum(static_cast<unsigned char>(s[left])) == false) {
                left++;
                continue;
            }
            else if (std::isalnum(static_cast<unsigned char>(s[right])) == false) {
                right--;
                continue;
            }
            else if (s[left++] != s[right--]) return false;
        }
        return true;
    }
};
