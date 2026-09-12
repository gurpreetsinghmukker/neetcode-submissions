class Solution:
    def trap(self, height: List[int]) -> int:
        
        p1 = 0
        p2 = 1

        lp = None
        # lt = None
        dh = None
        p_water = []
        start_collection = False
        water = 0
        for p1, _ in enumerate(height[:-1]):
            p2 = p1 +1
            # print(f"Heights-{height[p1]} - {height[p2]}")
            if (not start_collection) and height[p1]>height[p2]:
                # print("start_Coll")
                start_collection = True
                lp = p1
                # p_water.append(height[lp]- height[p2])
                # lt = p2
                # dh = True
                # level = False
                # p1 = p1+1
                # p2 = p2+1
            elif (not start_collection):
                # p1 = p1+1
                # p2 = p2+1
                continue

            if height[p2]<=height[p1]:
                # print("if")
                # lt = min(lt, p2)
                p_water.append(height[lp]- height[p2])


            elif height[p2]>height[p1] and height[p2]<height[lp]:
                p_water.append(height[lp]- height[p2])
                # print(f"elif-{p_water}")
                for i, p_h in enumerate(p_water):
                    if p_h > height[lp]-height[p2]:
                        water = water + p_h - (height[lp]-height[p2])
                        p_water[i] =(height[lp]-height[p2])

            elif height[p2]>=height[lp]:
                # print("elif2")
                lp = p2
                water = water + sum(p_water)
                p_water = []
                start_collection = False
            # print(f"{(p1,p2)},{water}-{p_water}-{lp}")
            # p1 = p1+1
            # p2 = p2+1
            
        # if p_water > 0:
        #     if p2<=lp and p2>lt:
        #         water = water + p_water - (lp-p2)*(height[lp]-height[p2])
    
        return water






