#include <iostream>
#include <map>
#include <string>

using namespace std;

class Logger {
public:
    Logger() {

    }
    
    bool shouldPrintMessage(int timestamp, string message) {
        auto it = this->m_mapMessages.find(message);
        //! Message already present in the map
        if (it != this->m_mapMessages.end()) {
            //! Message allowed - outside timestamp limit 
            if (timestamp - it->second >= 10) {
                this->m_mapMessages[message] = timestamp;
                return true;
            } else { //! Believe we dont need to track this, that may change
                return false;
            }
        }
        //! New message
        else {
            this->m_mapMessages[message] = timestamp;
            return true;
        }
    }
private:
    std::map<string, int> m_mapMessages;
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */

int main() {
    Logger* obj = new Logger();
    const bool param_1 = obj->shouldPrintMessage(0, "Hello World!");
    const bool param_2 = obj->shouldPrintMessage(9, "Hello World!");
    const bool param_3 = obj->shouldPrintMessage(10, "Hello World!");
    cout << "message accepted: " << param_1 << endl;
    cout << "message accepted: " << param_2 << endl;
    cout << "message accepted: " << param_3 << endl;
    return 0;
}
