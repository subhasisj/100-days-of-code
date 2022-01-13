class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
#         total_sum = sum(nums)
#         right = len(nums)-1
#         left = 0
#         while left < len(nums) and right > left:
#             current_sum = sum(nums[left:right])
#             if current_sum > total_sum:
#                 total_sum = current_sum
            
#             left+=1
#             right-=1
#         return total_sum
        max_sum = current_sum = nums[0]
        for i in range(1,len(nums)):
            current_sum = max(nums[i],current_sum + nums[i])
            max_sum = max(max_sum,current_sum)
            
        return max_sum
            
            