class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k=0
        for left in range(len(nums)):
            if nums[left] != val:
                nums[k] = nums[left]
                k+=1
        return k
                
    
    