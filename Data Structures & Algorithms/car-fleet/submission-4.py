class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        pos_speeds =  sorted(zip(position, speed), reverse= True, key = lambda x : x[0])
        fleets = []
        for i,ps in enumerate(pos_speeds):
            if not len(fleets):
                fleets.append([1, (target - ps[0])/ps[1]])
            else:
                time = fleets[-1][1]
                if (time*ps[1]+ps[0])>=target:
                    fleets[-1][0] = fleets[-1][0]+1
                else:
                    fleets.append([1,(target - ps[0])/ps[1]]) 
        return len(fleets)

        