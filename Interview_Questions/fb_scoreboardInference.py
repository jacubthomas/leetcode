def getMinProblemCount(N: int, S: List[int]) -> int:
    # The solution space is larger than it needs be, let's reduce and order
    scoreSet = set(S)
    orderedScoreSet = list(scoreSet)
    orderedScoreSet.sort(reverse=True)
    # Problem is limited by two factors
    # Factor 1: the number of 2s to make the highest score
    minNumberProblems = math.floor(orderedScoreSet[0])
    # Factor 2: if there are any odd scores
    for score in orderedScoreSet:
        if score & 1 == 1:
            minNumberProblems += 1
            break
    
    return minNumberProblems

# Some tests
print(getMinProblemCount(N=6, S=[1,2,3,4,5,6]))
print(getMinProblemCount(N=4, S=[4,3,3,4]))
print(getMinProblemCount(N=4, S=[2,4,6,8]))
print(getMinProblemCount(N=5, S=[2, 5, 3, 1, 5]))
