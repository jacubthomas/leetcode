from typing import List, Tuple
import sys
class DPSolution:
    def __init__ (self, V: List[int], N: int, C: int, S: float):
        self.N = N
        self.V = V
        self.C = C
        self.S = 1.0 - S
        self.memo = {}

    def solve(self, index: int, packageSum: float) -> float:

        # Base case: sell all packages, the last item and incur cost
        if index == self.N - 1:
            path1 = packageSum + self.V[index] - self.C  # Collect on last day
            path2 = 0.0  # Risk leaving
            return max(path1, path2)
        
        # Our memoization dict will have the unique of package batches
        # Since lists are mutable, we convert to tuple and store - so we only convert once!
        packageTuple = (index, packageSum)
        if packageTuple in self.memo:
            return self.memo[packageTuple]

        # Step forward, add todays package with old on hold, update decay of value
        path1 = self.solve(index+1, round((packageSum + self.V[index]) * self.S, 6))

        # Step forward, empty packages, get value of todays package plus others, pay cost
        path2 = self.solve(index+1, 0.0) + self.V[index] + packageSum - self.C

        # Select the max profitable solution path
        maxProfit = max (path1, path2)

        # Avoid doing this work again
        self.memo[packageTuple] = maxProfit

        return maxProfit

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    sum = 0
    # Simple cases
    # 1 No packages at risk
    if S == 0:
        for v in V:
            sum += v
        return sum - C

    # All packages will be stolen
    elif S == 1:
        for v in V:
            if v > C:
                sum += v - C
        return sum
    
    # The scale of this test requires that we extend the recursion depth allowed
    sys.setrecursionlimit(5000)
    dps = DPSolution(V, N, C, S)
    return round(dps.solve(0, 0.0), 6)

# Trivial Cases
print (getMaxExpectedProfit(5, [5, 5, 5, 5, 5], 5, 0))                        # 20
print (getMaxExpectedProfit(5, [5, 5, 1, 5, 5], 1, 1.0))                      # 16
print (getMaxExpectedProfit(N = 5, V = [10, 2, 8, 6, 4], C = 5, S = 0.0))     # 25
print (getMaxExpectedProfit(N = 5, V = [10, 2, 8, 6, 4], C = 5, S = 1.0))     # 9

# Provided test cases
print (getMaxExpectedProfit(N = 3, V = [10, 2, 8], C = 3, S = 0.5))           # 13 
print (getMaxExpectedProfit(N = 5, V = [10, 2, 8, 6, 4], C = 3, S = 0.5))     # 17
print (getMaxExpectedProfit(N = 5, V = [10, 2, 8, 6, 4], C = 3, S = 0.15))    # 20.10825
print (getMaxExpectedProfit(N = 100, V = [216, 185, 770, 627, 129, 646, 564, 224, 529, 229, 245, 738, 186, 225, 737, 33, 456, 510, 277, 248, 595, 66, 393, 480, 586, 971, 725, 689, 817, 776, 985, 983, 112, 877, 361, 687, 57, 652, 128, 302, 38, 920, 133, 216, 835, 102, 3, 766, 707, 419, 451, 907, 400, 804, 265, 892, 707, 398, 628, 966, 191, 285, 475, 541, 395, 694, 35, 763, 954, 299, 466, 293, 825, 433, 887, 54, 260, 795, 573, 95, 650, 77, 995, 740, 26, 569, 592, 793, 478, 987, 121, 890, 400, 792, 675, 316, 611, 29, 324, 433], C = 3, S = 0.15))
