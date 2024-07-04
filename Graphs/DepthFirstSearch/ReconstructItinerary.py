'''
Reconstruct Itinerary - LeetCode HARD

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight.
Reconstruct the itinerary in order and return it. All of the tickets belong to a man who departs from "JFK", thus, the itinerary must
begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when 
read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

Constraints:
1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
'''

from typing import Dict
from typing import List

class DFS:
    def __init__ (self, tickets: List[List[str]]):
        # We will need to keep track of the total number of stops
        # Given we have to use every path in solution itinerary
        self.numStops = len(tickets) + 1
        # Just for ease of reference
        self.tickets = tickets

    # We will use a map for adjacency reference - which airports connect to others 
    # To optimize efficiency, each list of connected airports will be sorted lexicographically
    def buildSortedAdjacencyMap(self) -> dict[str:List[str]]:
        # Build the initial adjacency map
        adjacencyMap = dict()
        for x in self.tickets:
            if x[0] not in adjacencyMap:
                adjacencyMap[x[0]] = [x[1]]
            else:
                adjacencyMap[x[0]].append(x[1])

        # Sort each list lexicographically
        for key in adjacencyMap:
            adjacencyMap[key].sort()

        return adjacencyMap


    def traverseAllSolutionPathsFromSource (self, currentPath: List[str], sortedAdjMap: dict[str:List[str]]) -> List[str]:
        # The solution MUST use every path provided once and only once!
        if len(currentPath) == self.numStops:
            return currentPath
        
        # Ease of readabily, pull out where we are now
        currentStop = currentPath[len(currentPath)-1]
        
        # To prevent crashing, abandon this path early if not a key in map
        if currentStop not in sortedAdjMap:
            return None
        
        # There will likely be repeats airports in long itinerary
        # We only need to try each once at each step in the journey
        avoidReattempt = set()
        
        # Consider all possible stops connected to this airport
        for stopIndex in range(len(sortedAdjMap[currentStop])):

            # Don't waste compute on something we already tried
            if sortedAdjMap[currentStop][stopIndex] not in avoidReattempt:
                # Temporarily remove this option from scope of possibility in deeper recursive levels
                stop = sortedAdjMap[currentStop].pop(stopIndex)
                # Temporarily add this to the solution path
                currentPath.append(stop)
                # Mark this airport as attempted once at this leg in the journey
                avoidReattempt.add(stop)
                # Recurse
                completeditinerary = self.traverseAllSolutionPathsFromSource(currentPath, sortedAdjMap)
                # Check if we're done and short circuit if so
                if (completeditinerary is not None and len(completeditinerary) == self.numStops):
                    return completeditinerary
                # Remove trialed stop from solution path
                currentPath.pop(len(currentPath)-1)
                # Add trialed stop back to the scope of possibility for later in the journey 
                sortedAdjMap[currentStop].insert(stopIndex, stop)

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dfs = DFS(tickets)
        sortedAdjMap = dfs.buildSortedAdjacencyMap()
        return dfs.traverseAllSolutionPathsFromSource(["JFK"], sortedAdjMap)
    
s = Solution()
s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]) #['JFK', 'MUC', 'LHR', 'SFO', 'SJC']
s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]) #['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) #['JFK', 'NRT', 'JFK', 'KUL']
s.findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]])#["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"]
s.findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]])
s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"]]) #['JFK', 'SFO', 'JFK', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL']




















# def traverseAllSolutionPathsFromSource (self, currentPath: List[str]) -> None:
    #     if len(currentPath) == self.numStops:
    #         self.solutionPaths.append(currentPath.copy())
    #         return
        
    #     currentStop = currentPath[len(currentPath)-1]
    #     self.visited[currentStop] += 1

    #     for stop in self.adjacencyMap[currentStop]:
    #         if self.visited[stop] < len(self.adjacencyMap[stop]):
    #             # Temporarily append this stop to currentPath
    #             currentPath.append(stop)
    #             # Recurse towards final stop
    #             self.traverseAllSolutionPathsFromSource(currentPath)
    #             currentPath.pop()

    #     self.visited[currentStop] -= 0
        # def shortestLexicograhicalPath(self) -> List[int]:
    #     shortestPath = self.solutionPaths[0]

    #     for i in range(1, len(self.solutionPaths)):
    #         for j in range(len(shortestPath)):
    #             if self.solutionPaths[i][j] < shortestPath[j]:
    #                 shortestPath = self.solutionPaths[i]
    #                 break
    #             elif self.solutionPaths[i][j] < shortestPath[j]:
    #                 continue
        
    #     return shortestPath