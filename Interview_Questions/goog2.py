import sys
from typing import List


def solution(S):

    # split list into chars
    li = list (S)
    # keep score
    max = 0
    # keeps track of unique chars on left 
    left = set ()
    # idea: only check score if next char adds nothing to set
    for i in range (0, len (S)):
        if S[i] in left:
            # no higher score feasible; return and save on runtime
            if max == 52:
                return max
            right = set (li[i:len (S)])
            score = len (left) + len (right)
            print (f"score = {score}; l={left}, r={right}")
            if score > max:
                max = score
        left.add (S[i])
    # edge case - string is composed of entirely unique chars
    if len (S) == len (left):
        max = len (S)
        # print (f"{max}! string was entirely unique")
    return max
'''
# Purely testing

print (solution ("he"))
print ()
solution ("hello")
print ()
solution ("bcac")
print ()
solution ("qwerty")
print ()
solution ("h")

import random
import string

def randStr(chars = string.ascii_lowercase, N=10):
	return ''.join(random.choice(chars) for _ in range(N))

default length(=10) random string
print(randStr())
random string of length 7
print(randStr(N=7)) 
print( solution (randStr (N=100000))) 
print (randStr (N=100000))

'''