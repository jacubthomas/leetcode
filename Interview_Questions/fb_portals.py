from typing import Deque, List, Set, Tuple

def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
    # First, let's gather all the portals so we know where to jump
    startCoordinate = []
    portalMap = createPortalMap(G, startCoordinate)

    # Let's solve with a BFS
    visited: Set[Tuple[int,int,int]] = set()
    queue: Deque[Tuple[int,int,int]] = Deque()
    # Avoid redundant work and inaccurate results, don't revisit grid squares 
    visited.add(tuple((startCoordinate[0], startCoordinate[1])))
    queue.append(tuple((startCoordinate[0], startCoordinate[1], 0)))
    while len(queue) > 0:
        # Get the current position
        coordinate = queue.popleft()
        # We have reached the end, return seconds
        if G[coordinate[0]][coordinate[1]] == "E":
            return coordinate[2]
        # Portal check
        if (isPortal(G, coordinate[0], coordinate[1]) and
            tuple((coordinate[0], coordinate[1])) in portalMap[G[coordinate[0]][coordinate[1]]]):
            # Add connecting portals to teleport to from here
            for portal in portalMap[G[coordinate[0]][coordinate[1]]]:
                if portal not in visited:
                    queue.append(tuple((portal[0], portal[1], coordinate[2] + 1)))
                    visited.add(portal)
        # For readability, build next coordinate tuples here
        up = tuple((coordinate[0]-1, coordinate[1]))
        left = tuple((coordinate[0], coordinate[1]-1))
        down = tuple((coordinate[0]+1, coordinate[1]))
        right = tuple((coordinate[0], coordinate[1]+1))

        # Go up
        if (coordinate[0] - 1 > -1 and 
            up not in visited and
            G[coordinate[0]-1][coordinate[1]] != "#"):
            queue.append(tuple((up[0], up[1], coordinate[2] + 1)))
            visited.add(up)
        # Go left
        if (coordinate[1] - 1 > -1 and 
            left not in visited and
            G[coordinate[0]][coordinate[1]-1] != "#"):
            queue.append(tuple((left[0], left[1], coordinate[2] + 1)))
            visited.add(left)
        # Go down
        if (coordinate[0] + 1 < R and 
            down not in visited and
            G[coordinate[0]+1][coordinate[1]] != "#"):
            queue.append(tuple((down[0], down[1], coordinate[2] + 1)))
            visited.add(down)
        # Go right
        if (coordinate[1] + 1 < C and
            right not in visited and
            G[coordinate[0]][coordinate[1]+1] != "#"):
            queue.append(tuple((right[0], right[1], coordinate[2] + 1)))
            visited.add(right)
    return -1

def createPortalMap(G: List[List[str]], startCoordinate: List[int]) -> dict:
    portalMap = {}
    for i in range(len(G)):
        for j in range(len(G[i])):
            # Portal detected
            if (isPortal(G,i,j)):
                if G[i][j] in portalMap:
                    portalMap[G[i][j]].append((i,j))
                else:
                    portalMap[G[i][j]] = [(i,j)]
            elif G[i][j] == "S":
                startCoordinate += [i, j] # [row, col]
    return portalMap

def isPortal(G: List[List[str]], row:int, col:int) -> bool:
    if (G[row][col] != "." and 
        G[row][col] != "S" and
        G[row][col] != "E" and 
        G[row][col] != "#"):
        return True
    else:
        return False

print(getSecondsRequired(R = 3, C = 3, G = [[".","E","."], 
                                            [".", "#", "E"], 
                                            [".", "S", "#"]]
                        ))

print(getSecondsRequired(R = 3, C = 4, G = [["a",".","S","a"],
                                            ["#","#","#","#"],
                                            ["E","b",".","b"]]
                        ))

print(getSecondsRequired(R = 3, C = 4, G = [["a","S",".","b"],
                                            ["#","#","#","#"],
                                            ["E","b",".","a"]]
                        ))

print(getSecondsRequired(R = 1, C = 9, G = [["x","S",".",".","x",".",".","E","x"]]))
