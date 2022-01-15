class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums) #keep the max of the list
        curr_min, curr_max = 1,1
        
        for n in nums:
            if n == 0:
                curr_min, curr_max = 1,1 #reset if 0 is encountered
                continue
            # n * curr_max can be +ve * +ve and n * curr_min can be -ve * -ve which can be a positive number 
            # we also take the current number n if all other are -ve's then if n is +ve, then n becomes max
            temp = curr_max*n # save the computation as it gets overwritten below
            curr_max = max(curr_max*n, curr_min*n, n) 
            # We also take the min here as current -ve number when multiplied by a next -ve number results in a +ve number
            curr_min = min(temp, curr_min*n, n)
            res = max(res, curr_max) # Keep the maximum till now
        return res
        
#         return curr_max
            # res = max(nums)
            # cur_min, cur_max = 1,1
            # for n in nums:
            #     if n == 0:
            #         cur_min, cur_max = 1,1
            #         continue
            #     temp = cur_max * n
            #     cur_max = max(n * cur_max, n * cur_min, n)
            #     cur_min = min(temp, n * cur_min, n)
            #     res = max(res, cur_max)
            # return res