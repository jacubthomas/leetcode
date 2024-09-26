
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        minLenBinaryString = a if len(a) < len(b) else b
        maxLenBinaryString = a if len(a) >= len(b) else b
        # print (f'min length {minLenBinaryString}, with len(a)={len(a)}, len(b)={len(b)}')
        
        minLenBinaryString = minLenBinaryString[::-1]
        maxLenBinaryString = maxLenBinaryString[::-1]
        
        solutionBinaryString = ""
        remainder = 0
        for i in range(len(minLenBinaryString)):
            minInt, maxInt = int(minLenBinaryString[i]), int(maxLenBinaryString[i])
            if minInt & maxInt:
                if remainder:
                    solutionBinaryString = "1" + solutionBinaryString
                else:
                    solutionBinaryString = "0" + solutionBinaryString
                remainder = 1
            elif minInt | maxInt:
                if remainder:
                    solutionBinaryString = "0" + solutionBinaryString
                else:
                    solutionBinaryString = "1" + solutionBinaryString
            else:
                if remainder:
                    solutionBinaryString = "1" + solutionBinaryString
                    remainder = 0
                else:
                    solutionBinaryString = "0" + solutionBinaryString
                    
        for j in range(len(minLenBinaryString), len(maxLenBinaryString)):
            maxInt = int(maxLenBinaryString[j])
            if remainder & maxInt:
                solutionBinaryString = "0" + solutionBinaryString
            elif remainder | maxInt:
                solutionBinaryString = "1" + solutionBinaryString
                remainder = 0
            else:
                solutionBinaryString = "0" + solutionBinaryString
                
        if remainder:
            solutionBinaryString = "1" + solutionBinaryString
        
        return solutionBinaryString
    
s = Solution()

print (s.addBinary("1011", "1010"))
assert s.addBinary("1011", "1010") == "10101"
print (s.addBinary("1011", "10"))
assert s.addBinary("1011", "10") == "1101"
print (s.addBinary("1", "11"))
assert s.addBinary("1", "11") == "100"
print (s.addBinary("100", "110010"))
assert s.addBinary("100", "110010") == "110110"