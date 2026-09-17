class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        pos_speeds =  sorted(zip(position, speed), reverse= True, key = lambda x : x[0])
        fleets = 0
        min_time = None
        for ps in pos_speeds:
            if not fleets:
                fleets = fleets + 1
                min_time = (target-ps[0])/ps[1]
            else:
                if (min_time*ps[1]+ps[0])<target:
                    min_time = (target - ps[0])/ps[1] 
                    fleets = fleets + 1
        return fleets

        