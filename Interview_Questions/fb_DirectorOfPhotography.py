from typing import List
def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    count = 0
    startingIndices = findAllPhotographersAndBackdrops(N, C)
    pStartingIndices, bStartingIndices = startingIndices[0], startingIndices[1]
    p_a_indices = []
    b_a_indices = []
    for startIndex in pStartingIndices:
        p_a_indices += findAllReachableActors(startIndex, N, C, X, Y)
        
    for startIndex in bStartingIndices:
        b_a_indices += findAllReachableActors(startIndex, N, C, X, Y)
        
    for midIndex in p_a_indices:
        count += findAllPBFromA("P", midIndex, N, C, X, Y)
        
    for midIndex in b_a_indices:
        count += findAllPBFromA("B", midIndex, N, C, X, Y)
        
    return count

def findAllPhotographersAndBackdrops(N: str, C: str) -> List[List[int]]:
    validPhotographerIndices = []
    validBackdropIndices = []
    for i in range(0, N):
        if C[i] == "P":
            validPhotographerIndices.append(i)
        elif C[i] == "B":
            validBackdropIndices.append(i)
        
    return [validPhotographerIndices, validBackdropIndices]

def findAllReachableActors(startIndex, N, C, X, Y) -> List[int]:
    a_indices = []
    for i in range(X, Y+1):
        indexWithOffset = startIndex + i
        # Don't exceed the length of the photography set
        if indexWithOffset >= N:
            break
        # Located a reachable, `artistic` actor from P or B
        if C[indexWithOffset] == "A":
            a_indices.append(indexWithOffset)
    return a_indices

def findAllPBFromA(startComponent: str, midIndex: int, N: int, C: int, X: int, Y: int) -> int:
    count = 0
    if startComponent == "P": # Photographer, PAB
        for i in range(X, Y+1):
            indexWithOffset = midIndex + i
            # Don't exceed the length of the photography set
            if indexWithOffset >= N:
                break
            # Located a reachable, `artistic` actor from P or B
            if C[indexWithOffset] == "B":
                count += 1
    elif startComponent == "B": # Backdrop, BAP
        for i in range(X, Y+1):
            indexWithOffset = midIndex + i
            # Don't exceed the length of the photography set
            if indexWithOffset >= N:
                break
            # Located a reachable, `artistic` actor from P or B
            if C[indexWithOffset] == "P":
                count += 1
    return count


print (getArtisticPhotographCount(N = 5, C = "APABA", X = 1, Y = 2))
print (getArtisticPhotographCount(N = 5, C = "APABA", X = 2, Y = 3))
print (getArtisticPhotographCount(N = 8, C = ".PBAAP.B", X = 1, Y = 3))
