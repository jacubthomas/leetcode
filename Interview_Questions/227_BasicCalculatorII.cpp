class Solution {
public:
    int calculate(string s) {
        //! Simplify life, remove all blank spaces in string
        std::erase(s, ' ');

        //! For readability, add operands into a set
        set<char> setCharOperands = { '+', '-', '*', '/' };

        //! Tokenize into 2 lists: nums and operands
        vector<int> vecIntNums1;
        vector<char> vecCharOperands1;
        int index = 0;
        string strNum = "";
        while (index < s.length()) {
            if (setCharOperands.count(s[index]) == 0) //! Not an operand
                strNum += s[index];
            else {
                vecIntNums1.push_back(stoi(strNum));
                strNum = "";
                vecCharOperands1.push_back(s[index]);
            }
            index++;
        }
        vecIntNums1.push_back(stoi(strNum)); //! Push final num

        if (vecCharOperands1.size() == 0) return vecIntNums1[0];

        //! Two passes, keeping order of operations
        //! First for multiplication and division
        vector<int> vecIntNums2;        // For the second pass
        vector<char> vecCharOperands2;  // For the second pass
        for (int idxNumLeft = 0, idxNumRight = 1, idxOperand = 0; 
            idxNumRight < vecIntNums1.size();  //! We can assume good inputs, so simple condition
             /**/) {

            //! Handle indefinite (* & /) chains, storing running value in right number
            while (idxOperand < vecCharOperands1.size() && 
                   (vecCharOperands1[idxOperand] == '*' || vecCharOperands1[idxOperand] == '/')) {
                if (vecCharOperands1[idxOperand] == '*')
                    vecIntNums1[idxNumRight] = vecIntNums1[idxNumLeft] * vecIntNums1[idxNumRight];
                else
                    vecIntNums1[idxNumRight] = vecIntNums1[idxNumLeft] / vecIntNums1[idxNumRight];
                idxNumLeft++;
                idxNumRight++;
                idxOperand++;
            }

            //! Edge case: end of the line, push last running value
            if (idxOperand == vecCharOperands1.size()) {
                vecIntNums2.push_back(vecIntNums1[idxNumLeft]);
                break;
            }

            //! Push number left of (+ or -) and operand onto structures for second sweep
            if (vecCharOperands1[idxOperand] == '+' || vecCharOperands1[idxOperand] == '-') { 
                vecCharOperands2.push_back(vecCharOperands1[idxOperand++]);
                vecIntNums2.push_back(vecIntNums1[idxNumLeft++]);
                idxNumRight++;
            }

            //! Edge case: end of the line, push last running value
            if (idxOperand == vecCharOperands1.size()) {
                vecIntNums2.push_back(vecIntNums1[idxNumLeft]);
                break;
            }
        }

        //! Second, add and subtract
        for (int idxNumLeft = 0, idxNumRight = 1, idxOperand = 0; 
            idxNumRight < vecIntNums2.size();  //! We can assume good inputs, so simple condition
             /**/) {
            if (vecCharOperands2[idxOperand] == '+')
                vecIntNums2[idxNumRight] = vecIntNums2[idxNumLeft] + vecIntNums2[idxNumRight];
            else
                vecIntNums2[idxNumRight] = vecIntNums2[idxNumLeft] - vecIntNums2[idxNumRight];
            idxNumLeft++;
            idxNumRight++;
            idxOperand++;
        }

        return vecIntNums2[vecIntNums2.size()-1];
    }
};
