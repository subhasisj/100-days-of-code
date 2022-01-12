class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        left = 1
        # right = 1
        for i in range(1,len(nums)):
            # left = right = nums[i]
            if nums[i-1] != nums[i]:
                nums[left] = nums[i]
                left+=1
            i+=1   
        return left
                    
        