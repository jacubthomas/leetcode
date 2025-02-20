from typing import List
import math

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    # Lock dynamics change for even or odd number of digits
    isEven = True if N % 2 == 0 else False 
    # Map out each digit's counterpoint in the lock
    counterPointList = findAllCounterPoints(N, M, C, isEven)
    # Sum each movement here for final result
    totalCostOfCombination: int = 0
    # We need the cost of each movement, so we track where we were last
    lastDigit = 1
    for nextDigit in C:
        # No moves necessary, no cost incurred
        if nextDigit == lastDigit:
            continue
        if isEven: # Even number digits on rotary lock
            # Next digit is the counterpoint
            if nextDigit == counterPointList[lastDigit]:
                totalCostOfCombination += math.floor(N / 2)
            # We are starting from the lower half of N
            elif lastDigit <= N / 2:
                if nextDigit < lastDigit:
                    totalCostOfCombination += lastDigit - nextDigit
                elif nextDigit > counterPointList[lastDigit]:
                    totalCostOfCombination += (lastDigit - 1) + (N - nextDigit) + 1
                else: # nextDigit < counterPointList[lastDigit]:
                    totalCostOfCombination += nextDigit - lastDigit
            # We are starting from the upper half of N
            else: # lastDigit > (N / 2):
                if nextDigit > lastDigit:
                    totalCostOfCombination += nextDigit - lastDigit
                elif nextDigit < counterPointList[lastDigit]:
                    totalCostOfCombination += (N - lastDigit) + (nextDigit - 1) + 1
                else: # nextDigit > counterPointList[lastDigit]:
                    totalCostOfCombination += abs(lastDigit - nextDigit)
        else: # Odd number digits on rotary lock
            if lastDigit == 1:
                # Upper half of rotary lock
                if nextDigit > math.ceil(N/2): 
                    totalCostOfCombination += N - nextDigit + 1
                # Lower half of rotary lock
                else:
                    totalCostOfCombination += nextDigit - 1
            # Next digit is the counterpoint
            elif nextDigit == counterPointList[lastDigit]:
                totalCostOfCombination += math.floor(N / 2)
            # We are starting from the lower half of N
            elif lastDigit <= math.ceil(N / 2):
                if nextDigit < lastDigit:
                    totalCostOfCombination += lastDigit - nextDigit
                elif nextDigit > counterPointList[lastDigit] and N != 3:
                    totalCostOfCombination += (lastDigit - 1) + (N - nextDigit) + 1
                else: # nextDigit < counterPointList[lastDigit]:
                    totalCostOfCombination += nextDigit - lastDigit
            # We are starting from the upper half of N
            else: 
                if nextDigit > lastDigit:
                    totalCostOfCombination += nextDigit - lastDigit
                elif nextDigit < counterPointList[lastDigit]:
                    totalCostOfCombination += (N - lastDigit) + (nextDigit - 1) + 1
                else: # nextDigit > counterPointList[lastDigit]:
                    totalCostOfCombination += lastDigit - nextDigit
        lastDigit = nextDigit
    return totalCostOfCombination


def findAllCounterPoints(N: int, M: int, C: List[int], isEven: bool):
    # Store our counterpoint key in here
    # Counterpoints will help us determine the optimal route
    counterPointList = [-1 for x in range(0, N+1)]
    if isEven:
        for digit in range(1, math.floor(N/2) + 1):
            digitCounterPoint = digit + math.floor(N/2)
            counterPointList[digit] = digitCounterPoint
            counterPointList[digitCounterPoint] = digit
    else:
        for digit in range(1, math.ceil(N/2) + 1):
            digitCounterPoint = digit + math.floor(N/2)
            counterPointList[digit] = digitCounterPoint
            counterPointList[digitCounterPoint] = digit
    return counterPointList

print (getMinCodeEntryTime(N = 3, M = 3, C = [1, 2, 3]))
print (getMinCodeEntryTime(N = 5, M = 3, C = [1, 5, 3, 4]))
print (getMinCodeEntryTime(N=10, M=3, C=[1,6,1]))
print (getMinCodeEntryTime(N = 10, M = 4, C = [9, 4, 4, 8]))
print (getMinCodeEntryTime(N = 10, M = 4, C = [9, 4, 4, 8, 8, 6]))
