class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = []
        ends = []
        for i in intervals:
            starts.append(i[0])
            ends.append(i[1])
        
        starts.sort()
        ends.sort()
        s = e = 0
        numRooms = available = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                if available == 0:
                    numRooms += 1
                else:
                    available -= 1
                    
                s += 1
            else:
                available += 1
                e += 1
        
        return numRooms