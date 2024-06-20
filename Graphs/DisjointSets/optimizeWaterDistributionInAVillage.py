'''
Leetcode difficulty: HARD
Runtime: Beats 98.09% of python3 submissions
Memory: Beats 98.85% of python3 submissions
There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.
For each house i, we can either build a well inside it directly with cost wells[i - 1] (note the -1 due to 0-indexing), 
or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes where 
each pipes[j] = [house1j, house2j, costj] represents the cost to connect house1j and house2j together using a pipe. 
Connections are bidirectional, and there could be multiple valid connections between the same two houses with 
different costs. Return the minimum total cost to supply water to all houses.

Example 1:
Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3
Explanation: The image shows the costs of connecting houses using pipes.
The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with 
cost 2 so the total cost is 3.

Example 2:
Input: n = 2, wells = [1,1], pipes = [[1,2,1],[1,2,2]]
Output: 2
Explanation: We can supply water with cost two using one of the three options:
Option 1:
- Build a well inside house 1 with cost 1.
- Build a well inside house 2 with cost 1.
The total cost will be 2.
Option 2:
- Build a well inside house 1 with cost 1.
- Connect house 2 with house 1 with cost 1.
The total cost will be 2.
Option 3:
- Build a well inside house 2 with cost 1.
- Connect house 1 with house 2 with cost 1.
The total cost will be 2.
Note that we can connect houses 1 and 2 with cost 1 or with cost 2 but we will always choose the cheapest option. 

Constraints:
2 <= n <= 104
wells.length == n
0 <= wells[i] <= 105
1 <= pipes.length <= 104
pipes[j].length == 3
1 <= house1j, house2j <= n
0 <= costj <= 105
house1j != house2j
'''

from typing import List
from typing import Set
from typing import Tuple

class UnionFind:
    def __init__ (self, weight: List[int]) -> None:
        self.root = [x for x in range(len(weight))]
        self.weight = weight

    def find (self, x: int) -> Tuple[int,int, int, int]:
        # Node is a true root, its root is itself
        if x == self.root[x]:
            return x, self.weight[x], x, self.weight[x]
        
        # Look for true root and the largest cost along the way
        recursionResults = self.find(self.root[x])

        # Compress path, so this node points to its true root
        self.root[x] = recursionResults[0]

        # Reevaluate the largest cost along the way
        maxWeightIndex = recursionResults[2]
        if self.weight[recursionResults[2]] < self.weight[x]:
            maxWeightIndex = x

        # Return results
        return self.root[x], self.weight[self.root[x]], maxWeightIndex, self.weight[maxWeightIndex]
    
    def union (self, connection: List[int]) -> None:

        # Find each node's true root and max cost along each path to that root
        xRoot, yRoot = self.find(connection[0] - 1), self.find(connection[1] - 1)

        # Houses are not already connected - we will always connect
        if xRoot[0] != yRoot[0]: #and connection[2] <= xRoot[3] or connection[2] <= yRoot[3]:
            # xRoot will house the well 
            if xRoot[1] <= yRoot[1]:
                self.root[yRoot[0]] = xRoot[0]
            # yRoot will house the well
            else:
                self.root[xRoot[0]] = yRoot[0]
            
            # Cost of pipe will cheapen the cost of connection somewhere along the line
            # Just because we connect two properties, does not mean we will immediately the pay the piping cost
            # If pipe is more expensive than in house well, leave as is
            if connection[2] <= xRoot[3] or connection[2] <= yRoot[3]:
                # Update the most expensive connection along the way
                if xRoot[3] > yRoot[3]:
                    self.weight[xRoot[2]] = connection[2]
                else:
                    self.weight[yRoot[2]] = connection[2]

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # Sort the pipes by connection cost ascending
        # This will help ensure that we prioritize cheaper connections
        pipes = sorted(pipes, key=lambda x: x[2])

        # Unite houses into disjoint sets and handle costs
        uf = UnionFind(wells)
        for p in pipes:
            uf.union(p)

        # Sum costs for end result
        result = 0
        for x in wells:
            result += x

        return result

s = Solution()

# Case 1: cheaper to connect pipes from 0th house well 
print(s.minCostToSupplyWater(3, [1,2,2], [[1,2,1],[2,3,1]])) # 3
# Case 2: more than one option for optimal cost
print(s.minCostToSupplyWater(2, [1,1], [[1,2,1],[1,2,2]])) # 2
# Case 3: cheaper to connect pipes from 0th house well, some connections cost more than others
print(s.minCostToSupplyWater(4, [1,2,2,3], [[1,2,1],[2,3,1],[3,4,2]])) # 5
# Case 4: cheaper to connect pipes from nth house well
print(s.minCostToSupplyWater(4, [2,3,3,1], [[1,2,1],[2,3,1],[3,4,1]])) # 4
# Case 5: multiple pipe connections and a standalone house well in between w->p w p<-w
print(s.minCostToSupplyWater(5, [1,3,2,3,1], [[1,2,1],[3,4,1]])) # 6
# Case 6: multiple pipe connections and a standalone house well in between w->p p- w ->w
print(s.minCostToSupplyWater(5, [46012,72474,64965,751,33304], [[2,1,6719],[3,2,75312],[5,3,44918]])) # 131704
# Case 7: 
print(s.minCostToSupplyWater(6, [4625,65696,86292,68291,37147,7880], [[2,1,79394],[3,1,45649],[4,1,75810],[5,3,22340],[6,1,6222]])) # 204321

print(s.minCostToSupplyWater(
60, 
[93151,20876,59743,57253,22852,68389,7424,54743,32955,39509,14896,54179,51356,78618,95595,69161,37790,67284,91644,91111,52096,61039,56597,70549,72491,90473,42299,76091,89905,31271,58546,48511,72171,78695,41038,81168,32922,49332,637,7340,70333,20202,45698,64674,12549,46263,26798,1334,30355,83189,26439,51031,85145,56095,38430,79718,82385,25719,97525,82106],
[[2,1,21154],[3,2,81115],[4,3,94841],[5,2,96414],[6,3,72515],[7,5,52265],[8,1,60281],[9,5,47008],[10,6,83062],[11,1,83592],[12,11,29667],[13,5,43482],[14,8,68029],[15,6,29058],[16,14,14198],[17,8,61513],[18,10,96383],[19,3,12103],[21,11,51835],[22,8,14803],[23,22,30324],[24,23,63187],[25,21,62508],[26,13,86421],[27,22,59810],[28,6,80818],[29,25,350],[30,26,9676],[31,27,11396],[33,29,39112],[34,18,35099],[35,3,79588],[36,25,93238],[37,30,18366],[38,16,57918],[39,36,14416],[40,25,27362],[41,5,12434],[42,9,5570],[43,42,72309],[44,8,81276],[45,44,2620],[46,44,57766],[47,11,71293],[48,40,14627],[49,48,33901],[52,49,70471],[53,38,6615],[55,19,77453],[56,9,63999],[57,34,10940],[58,29,43449],[59,43,22295],[60,5,84242]]
))

print(s.minCostToSupplyWater(
50,
[57470,22135,39059,13746,93579,37060,41410,48513,26402,49607,63789,97197,91704,95909,95206,82668,73090,48372,94304,17775,57674,6017,89121,51409,67350,12884,58013,98902,40347,52361,46649,11588,29961,86814,87530,49581,40742,41808,2417,77039,39923,80279,96771,61659,58972,89390,22527,10042,45414,78278],
[[2,1,30756],[3,2,2883],[4,2,3478],[5,2,29321],[6,2,47542],[7,5,35806],[8,5,26531],[9,3,16321],[10,4,82484],[11,2,55920],[12,6,21253],[13,5,90537],[14,12,83795],[15,14,70353],[16,14,76983],[17,13,63416],[18,4,39590],[19,10,86794],[20,19,31968],[21,4,32695],[22,10,40287],[23,20,27993],[24,3,86349],[25,3,52080],[26,2,86798],[27,6,93012],[28,17,87517],[29,27,33298],[30,20,40408],[31,20,3601],[32,27,26667],[33,14,46235],[34,28,4118],[35,19,71371],[36,3,56630],[37,19,56934],[38,32,64916],[39,15,12873],[40,1,13404],[41,28,84906],[42,9,29830],[43,33,35222],[44,43,93296],[45,6,68101],[46,1,14170],[47,21,88398],[48,16,36713],[49,46,87642],[50,47,79170],[40,44,55496],[35,46,14494],[22,43,35515],[5,32,66988],[4,28,2710],[4,49,22546],[8,19,86828],[24,28,94750],[17,34,5150],[27,47,11319],[18,23,67878],[5,46,39486],[20,41,4537],[13,34,2134],[13,20,64453],[46,47,15637],[20,45,994],[21,22,24603],[23,25,68916],[8,14,25581],[15,28,80808],[33,48,45189],[14,38,3176],[10,22,12081],[13,15,73530],[6,36,67511],[27,38,76774],[6,21,21673],[28,49,72219],[40,50,9568],[31,37,66173],[14,29,93641],[4,40,87301],[18,46,41318],[2,8,25717],[1,7,3006],[8,28,57525],[22,47,87434],[14,28,90336],[17,28,76566],[1,15,621],[3,43,9840],[28,48,6760],[35,41,8100],[45,50,37009],[18,20,51872],[13,19,22254],[3,37,83689],[5,34,97516],[27,32,69991],[6,40,87955],[2,18,85693],[5,37,50456],[8,20,59182],[16,38,58363],[9,39,58494],[39,43,73017],[10,15,88526],[16,23,48361],[3,23,4869],[6,50,63469],[38,49,92016],[7,43,54692],[11,47,54058],[6,20,89397],[13,41,45087],[10,32,40252],[3,40,44901],[13,45,89230],[13,24,66162],[14,18,8764],[23,30,23278],[34,43,79826],[8,48,64979],[2,39,96383],[9,29,8989],[11,40,33869],[29,35,17176],[28,42,55592],[3,45,6236],[32,38,15661],[10,39,21387],[39,48,96338],[12,35,60793],[10,24,15572],[15,27,2876],[32,33,45576],[43,46,62828],[9,35,66854],[13,14,13987],[12,49,52498],[20,38,13821],[9,24,60065],[10,43,40493],[9,10,58114],[29,32,82689],[7,47,71961],[14,41,82402],[20,33,38732],[14,45,75027],[6,26,71464],[17,42,54322],[15,21,91938],[19,26,29988],[13,22,35995],[1,25,30943],[27,46,52169],[11,17,7684],[26,31,74435],[17,43,45487],[7,42,77480],[12,40,93413],[37,50,79889],[1,18,96870],[13,31,83310],[37,42,72111],[13,28,63010],[22,41,94896],[3,6,34794],[36,47,43873],[12,24,25206],[11,38,68925],[8,42,81491],[4,5,20441],[1,29,40420],[9,32,86923],[3,50,4554],[2,17,94357],[22,30,90132],[14,15,61438],[15,20,51869],[19,20,15101],[22,25,6103],[8,49,11497],[11,32,22278],[35,44,56616],[4,15,55379],[20,49,35085],[43,48,61499],[17,26,18614],[24,43,13360],[24,47,59846],[28,43,36311],[17,25,63309],[1,14,30207],[26,44,68497],[33,36,49911],[23,40,24286],[15,19,30436],[29,34,36508],[27,40,1263],[30,42,82615],[28,46,19622],[16,45,23915],[40,43,90161],[26,30,59013],[26,38,43794],[26,36,92972],[18,24,12283],[3,22,66380],[15,30,39474],[11,35,82661],[12,50,84860],[14,26,25992],[16,39,33166],[37,43,66029],[25,37,36524],[35,40,13180],[27,43,30431],[14,19,36848],[6,16,14528],[10,42,88113],[30,36,36002],[13,36,65864],[26,48,44068],[4,26,41258],[19,29,63750],[3,34,73378],[13,16,90339],[28,37,31401],[22,37,80956],[18,35,51968],[37,49,36399],[18,42,37774],[1,30,24687],[23,43,55470],[6,47,69677],[21,39,6826],[15,24,38561],[9,11,59617],[21,24,31175],[18,30,84104],[10,33,25157],[18,31,50861],[25,26,84920],[18,19,46874],[4,13,182],[17,50,34211],[31,47,65093],[22,50,1070],[12,16,36510]]
))











'''
def union (self, connection: List[int]) -> None:
        xRoot, yRoot = self.find(connection[0] - 1), self.find(connection[1] - 1)

        # Houses are not already connected
        if xRoot[0] != yRoot[0]:

            
            if xRoot[1] < yRoot[1] and connection[2] <= yRoot[1]:
                self.root[yRoot[0]] = xRoot[0]
                self.weight[yRoot[0]] = connection[2]
            elif yRoot[1] < xRoot[1] and connection[2] <= xRoot[1]:
                self.root[xRoot[0]] = yRoot[0]
                self.weight[xRoot[0]] = connection[2]

'''