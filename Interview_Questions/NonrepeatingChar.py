# class Solution:

def firstUniqChar(s: str) -> int:
   
    # array of uniques
    unq = []
    rpt = []

    # consider at each element 
    for i in s:
        # i might be unique
        if i not in unq and i not in rpt: 
            unq.append(i)
        # i is not unique
        elif i in unq:
            unq.remove(i) 
            rpt.append(i)
    # look for first unique 
    for i in range(len(s)):
        if s[i] in unq:
            return i

    # no unique chars in s
    return -1
    
firstUniqChar("aadadaad")
