class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        
        while l<r:
            area = (r-l) * min(height[l],height[r]) #Calculate area len x bdth , we take min of the height of the containers as water will                                                     # spill
            res = max(res, area) # Take the max area till now
            
            if height[l] < height[r]: #if left most height is less than right then move left or move from right towards left
                l+=1
                
            else:
                r-=1
        return res
         