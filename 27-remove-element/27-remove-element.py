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
                
    
#     def removeElement(self, nums: List[int], val: int) -> int:
        
#         k=0
#         for left in range(len(nums)):
#             if nums[left] != val:
#                 nums[k] = nums[left]
#                 k+=1
#         return k