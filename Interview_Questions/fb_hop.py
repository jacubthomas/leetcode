from typing import List
def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    # Handle trivial case - 1 frog
    if F == 1:
        return N - P[0]

    # Sort the frogs from furthest lilypad -> closest to shore
    P.sort()

    # Stores result
    hopCount = 0

    # The most optimal approaches is for frogs to cluster together
    clusterCoordinates = [P[0],P[0]]

    # Get all the frogs in one mass
    nextFrog = 1
    while (clusterCoordinates[1] != P[len(P) - 1]):
        hopCount += clusterFrogs(P, clusterCoordinates, nextFrog)
        nextFrog += 1

    # Take final leaps
    hopCount += (N - 1 - clusterCoordinates[1]) + F

    return hopCount

def clusterFrogs(P: List[int], clusterCoordinates: List[int], nextFrog: int) -> int:
    hopCount = 0
    if P[nextFrog] - clusterCoordinates[1] > 1:
        hopCount += P[nextFrog] - clusterCoordinates[1] - 1
    clusterCoordinates[1] = P[nextFrog]
    return hopCount

print(getSecondsRequired(N = 3, F = 1, P = [1]))                # 2
print(getSecondsRequired(N = 3, F = 2, P = [1, 2]))             # 2
print(getSecondsRequired(N = 4, F = 2, P = [1, 2]))             # 3
print(getSecondsRequired(N = 6, F = 3, P = [5, 2, 4]))          # 4
print(getSecondsRequired(N = 7, F = 3, P = [5, 2, 4]))          # 5
print(getSecondsRequired(N = 10, F = 4, P = [5, 1, 4, 8]))      # 9
