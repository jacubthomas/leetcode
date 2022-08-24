import sys
import random
from typing import List

def solution(A):

    # Put everything in map. Tuple the values. Speed up search time.
    A_dict = {}
    for x in range (0, len (A)):
        A_dict[A[x]] = x

    # sum distance by looping through map from start to finish
    distance = 0
    for i in range(1, len (A)):
        j = i + 1
        distance += abs (A_dict[i] - A_dict[j])

    return distance

''' # Purely testing
print (solution ([4,2,1,3]))
print (solution ([1]))
print (solution ([3, 5, 4, 2, 1]))

l = []
for i in range (1, 100000000):
    l.append (i)

# print (l)

random.shuffle (l)

# print (l)

print (solution (l))
'''