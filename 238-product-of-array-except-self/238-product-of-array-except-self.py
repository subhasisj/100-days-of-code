import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product_list = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            product_list[i] = prefix
            prefix*= nums[i]
        
        post_fix = 1
        for i in range(len(nums)-1,-1,-1):# Dont include the last element as there is nothing right to it and loop in reverse till the last but one element
            product_list[i] *= post_fix
            post_fix*= nums[i]        
            
        
        return product_list