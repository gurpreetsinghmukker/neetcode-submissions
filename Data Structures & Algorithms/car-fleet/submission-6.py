class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        pos_speeds =  sorted(zip(position, speed), reverse= True, key = lambda x : x[0])
        fleets = 0
        min_time = None
        for p,s in pos_speeds:
            if not fleets:
                fleets = fleets + 1
                min_time = (target-p)/s
            else:
                if (min_time*s+p)<target:
                    min_time = (target - p)/s 
                    fleets = fleets + 1
        return fleets

        