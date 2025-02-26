'''
Difficulty Medium
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:
1 <= intervals.length <= 104
0 <= starti < endi <= 106

Note that meeting boundaries are exclusive. That is, [0, 30], [30, 45] only requires 1 meeting room.

Below are 3 solutions to the given problem, however, the `NaiveSolution` will likely not scale well
'''

from typing import List
import math

class TwoPointerSolution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # End result stored here
        meetingRooms = 0

        # Let's track two pointers - 1) on meeting start times 2) on meeting end times
        meetingStartTimes, meetingEndTimes = [], []
        for meeting in intervals:
            meetingStartTimes.append(meeting[0])
            meetingEndTimes.append(meeting[1])
        
        # We want to proceed with two pointers moving along an ordered timeline
        meetingStartTimes.sort()
        meetingEndTimes.sort()

        # Consider each meeting start
        endedMeetingIndex = 0
        for time in meetingStartTimes:
            # A meeting has not ended prior to this starting - so no free rooms
            if time < meetingEndTimes[endedMeetingIndex]:
                meetingRooms += 1
            # A meeting has ended and a room has freed up, note the meeting end by incrementing index
            else:
                endedMeetingIndex += 1
        
        return meetingRooms
    
class DecentSolution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Resulting count of minimum number of meeting rooms
        totalMeetingRooms = 0
        openMeetingRooms = 0

        openIntervalIndex = 0
        closeIntervalMap = {}

        # Order the input intervals by meeting start time
        intervals.sort(key=lambda x: x[0])

        minInterval, maxInterval = math.inf, 0
        # Determine the range of meetings for a day
        for interval in intervals:
            minInterval = min(minInterval, interval[0])
            maxInterval = max(maxInterval, interval[1])

        # Loop over the day entire
        for current_time in range (minInterval, maxInterval + 1):
            # Close any meetings that are ending now
            # Pop returns the value, 0 if not found, and removes the kv-pair from map
            openMeetingRooms += closeIntervalMap.pop(current_time, 0)

            # Open any meetings that are starting now
            while (openIntervalIndex < len(intervals) and 
                   intervals[openIntervalIndex][0] == current_time):
                # Not enough meeting rooms allocated - allocate another
                if openMeetingRooms == 0:
                    totalMeetingRooms += 1
                # Enough meeting rooms allocated - take a free room
                else:
                    openMeetingRooms -= 1
                if intervals[openIntervalIndex][1] in closeIntervalMap:
                    closeIntervalMap[intervals[openIntervalIndex][1]] += 1
                else:
                    closeIntervalMap[intervals[openIntervalIndex][1]] = 1
                openIntervalIndex += 1
                
        return totalMeetingRooms    

class NaiveSolution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        prefixWindow = []
        maxOverlaps = 1 if len(intervals) > 0 else 0

        for interval in intervals:
            for i in range(interval[0]-1, interval[1]):
                if i >= 0 and i < len(prefixWindow):
                    prefixWindow[i] += 1
                    maxOverlaps = max(maxOverlaps, prefixWindow[i])
                else:
                    break
            # Prefix Window is smaller than interval start & end
            if len(prefixWindow) < interval[1]:
                expansionSize = interval[1] - len(prefixWindow)
                unmarkedNewTerritory = interval[0] - len(prefixWindow)
                windowExtension = [0 if x < unmarkedNewTerritory else 1 for x in range(expansionSize)] 
                prefixWindow.extend(windowExtension)
        
        return maxOverlaps

s = TwoPointerSolution()


print(s.minMeetingRooms([[7,10],[2,4]]))                        # 1
print(s.minMeetingRooms([[0,30],[5,10],[15,20]]))               # 2
print(s.minMeetingRooms([[0,30], [30,45]]))
print(s.minMeetingRooms([[0,30], [35,45]]))
print(s.minMeetingRooms([[0,30]]))
print(s.minMeetingRooms([[30,45], [25,35], [0,30]]))
print(s.minMeetingRooms(intervals = [[666908, 955224], [115899, 698516], [594694, 900250], [760163, 812415], [753392, 921621], 
             [552708, 739597], [239441, 723233], [426731, 921876], [939755, 951655], [568913, 724940], 
             [35097, 742180], [337917, 489417], [506621, 599607], [901322, 957802], [919780, 947474], 
             [377187, 385526], [976493, 982275], [218965, 653833], [341277, 859224], [20305, 448497], 
             [710076, 765249], [199704, 397451], [727764, 828225], [918998, 994988], [55895, 712797], 
             [168437, 346151], [317717, 554263], [776812, 853428], [674568, 840913], [22802, 182370], 
             [983337, 992700], [202843, 586787], [393882, 585400], [479804, 599782], [55129, 631483], 
             [127570, 183602], [924398, 935480], [636221, 728145], [653502, 820506], [972452, 991754], 
             [346926, 786271], [864961, 909961], [763376, 932999], [660162, 857284], [665638, 996619], 
             [382044, 725095], [648361, 738600], [842036, 893194], [793916, 861600], [183472, 391354], 
             [389943, 403962], [935732, 957773], [255881, 339676], [507604, 629530], [43403, 446407], 
             [572703, 800748], [179961, 917790], [604247, 774754], [867485, 943705], [931418, 996266], 
             [529902, 549886], [628203, 909185], [273953, 537152], [485791, 493131], [962240, 992857], 
             [805648, 957234], [864435, 993905], [380163, 394636], [365912, 696614], [692780, 763690], 
             [88391, 175510], [517516, 997996], [55785, 220926], [332016, 884045], [978729, 997186], 
             [628745, 772059], [79076, 590936], [693202, 803197], [830751, 906570], [411192, 926634], 
             [505636, 866144], [491507, 695696], [233626, 612341], [801905, 903623], [803267, 861590], 
             [187837, 386921], [804403, 897981], [624092, 920557], [776114, 820505], [829421, 983321], 
             [523259, 659313], [439618, 939703], [656412, 847529], [738818, 905493], [456974, 959987], 
             [49819, 785896], [359097, 795832], [968097, 971405], [273593, 878435], [123365, 891763], 
             [145239, 333518], [320009, 732584], [645431, 659800], [642698, 798106], [575751, 620799], 
             [265917, 515166], [338354, 657257], [594910, 620141], [311231, 926660], [384251, 391272], 
             [414238, 660846], [668398, 831747], [539710, 835849], [611474, 623349], [928001, 958153], 
             [696951, 896466], [95310, 432758], [126077, 812875], [630979, 937825], [378800, 495762], 
             [477182, 611848], [176658, 266914], [159230, 866198], [599339, 648395], [657021, 674767], 
             [878318, 973086], [945526, 949921], [531114, 833957], [603997, 787536], [255572, 344957], 
             [554043, 597121], [514062, 788977], [231056, 829713], [511899, 605072], [230760, 251700], 
             [186101, 683937], [207309, 292586], [571977, 923750], [236581, 713398], [387637, 658802], 
             [864660, 991952], [700847, 820583], [412887, 669848], [945271, 993787], [964910, 982894], 
             [2348, 738969], [833879, 938414], [166617, 327128], [489390, 565120], [770584, 987333], 
             [460613, 640994], [868555, 949974], [925419, 951560], [531025, 647051], [982586, 989884], 
             [964274, 985389], [350420, 367991], [819048, 982876], [253837, 804564], [812434, 842410], 
             [778796, 784927], [152406, 822948], [738465, 950470], [80769, 527424], [959707, 993280], 
             [773417, 937029], [518265, 763937], [181373, 479735], [935255, 996949], [734769, 954039], 
             [272335, 498723], [549609, 941478], [768712, 885403], [433313, 604372], [640922, 984873], 
             [580810, 768123], [537709, 607741], [117473, 301447], [299379, 382111], [651326, 748675], 
             [700024, 978844], [543142, 667137], [655144, 736210], [566233, 895043], [984653, 996849], 
             [770712, 917457], [818054, 980279], [702524, 973662], [223422, 985190], [493710, 635293], 
             [774751, 798372], [517143, 882947], [375436, 538046], [364076, 808791], [683904, 908417], 
             [995567, 999006], [116180, 738398], [488035, 852087], [657811, 791635], [182854, 258830]]))
