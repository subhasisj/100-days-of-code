class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i,a in enumerate(nums):
            # if its not the 1st element and it is the same as the next one
            if i>0 and a == nums[i-1]: 
                continue
             
            l,r = i+1, len(nums)-1 
            while l<r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0: # if the sum > 0 then the expected sum has to be with an element in the left as this is sorted
                    r-=1
                elif threesum < 0: # if the sum < 0 then the expected sum has to be with an element in the right as this is sorted
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res
                    
                                 
                                 