class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
#         non_val_elements = sum(map(lambda i: i!= val,nums))
        
#         right = len(nums)-1
        
#         for left in range(len(nums)):
#             if nums[left] == val:
#                 if nums[right] != nums[left]:
#                     nums[left],nums[right] = nums[right],nums[left]
#                 else:
#                     right-=1
#             left+=1
#         print(left)
#         return left
        k=0
        for left in range(len(nums)):
            if nums[left] != val:
                nums[k] = nums[left]
                k+=1
        return k
                
    
    