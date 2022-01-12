class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind = 0
        while ind < len(nums):
            # ind+=1
            if nums[ind] == val:
                nums.remove(val) # Remove the first matching element
                continue
            ind+=1
        return len(nums)
                
    
    