from typing import List
import math

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # The problem is easier with a little order
    S.sort()

    # We will move through the problem with a lens in between diners 
    # First case, between table edge and first diner
    diner2Index = 0
    diner1, diner2 = -1, S[diner2Index]

    # The diners we can add will accumulate here
    additionalDiners = 0
    for i in range(0, len(S)):
        # Increment our diner lens
        if i != 0:
            diner1, diner2 = S[diner2Index-1], S[diner2Index]
        # Find any open spots
        additionalDiners += findAndAssignNewDiners(False, N, K, S, diner1, diner2)
        # Prepare for next iteration
        diner2Index += 1

    # Last case, between last diner and table edge
    diner1, diner2 = S[diner2Index-1], -1
    additionalDiners += findAndAssignNewDiners(False, N, K, S, diner1, diner2)

    return additionalDiners

def findAndAssignNewDiners(isForward: bool, 
                            N: int, 
                            K: int, 
                            S: List[int], 
                            diner1: int, 
                            diner2: int) -> int:
    additionalDiners: int = 0
    # Left Edge of table
    if diner1 == -1:
        if diner2 > K+1:
            additionalDiners += math.floor((diner2-1) / (K+1))
    # Right Edge of table
    elif diner2 == -1:
        additionalDiners += math.floor((N - diner1) / (K + 1))

    # In between preexisting two diners
    else: 
        if diner1 + K + 1 <= diner2 - K - 1:
            additionalDiners += math.floor((diner2 - (diner1 + K + 1)) / (K + 1))
    return additionalDiners

print (getMaxAdditionalDinersCount(N = 10, K = 1, M = 2, S = [2, 6]))
print (getMaxAdditionalDinersCount(N = 15, K = 2, M = 3, S = [11, 6, 14]))
print (getMaxAdditionalDinersCount(N = 17, K = 2, M = 2, S = [13, 6]))
print (getMaxAdditionalDinersCount(N = 22, K = 2, M = 2, S = [15, 8]))

#       O        X        O           X        O
# __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
# 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17


#     O       O        X        O           X        O        O
# __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __
# 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22
