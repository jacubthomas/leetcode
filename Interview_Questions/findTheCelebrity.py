'''
Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.
Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
You are given a helper function bool knows(a, b) that tells you whether a knows b. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.
Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.

Example 1:
Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Example 2:
Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.

Constraints:
n == graph.length == graph[i].length
2 <= n <= 100
graph[i][j] is 0 or 1.
graph[i][i] == 1

Follow up: If the maximum number of allowed calls to the API knows is 3 * n, could you find a solution without exceeding the maximum number of calls?
'''

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # Consider all attendees as possible celebrities
        possibleCelebSet = set()
        for x in range(0,n):
            possibleCelebSet.add(x)

        # Eliminate all attendees down to 1 possible celeb with only n calls to api
        # Each loop iteration reduces scope of possibility by 1
        while len(possibleCelebSet) > 1:
            # Pull two candidates from the set
            possibleCeleb1, possibleCeleb2 = possibleCelebSet.pop(), possibleCelebSet.pop()
            # A knows B, then A cannot be a celebrity - celebrity knows no one but themself
            if knows(possibleCeleb1, possibleCeleb2):
                possibleCelebSet.add(possibleCeleb2)
            # A doesn't know B, then B cannot be a celebrity - everyone knows the celebrity
            else:
                possibleCelebSet.add(possibleCeleb1)

        # Consider final candidate with <= 2 * n calls
        celeb = possibleCelebSet.pop()
        for i in range (0,n):
            # Everyone knows themself
            if i == celeb:
                continue
            # Someone doesn't know candidate, so they're not a celeb
            elif knows(i, celeb) == False:
                return -1
            # Candidates know someone, so they're not a celeb (who knows no one but themself)
            elif knows(celeb, i) == True:
                return -1
        return celeb