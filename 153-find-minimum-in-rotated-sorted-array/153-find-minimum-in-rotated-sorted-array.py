class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0,len(nums)-1 
        
        #  Run binary search 
        while l <= r:
#              if subarray is already sorted
            if nums[l] < nums[r]:
#              We take the left most element as it is already sorted
                res = min(res, nums[l])
                break
#             In case the array is not sorted
            mid = (l+r) // 2 # Take the middle element
            res = min(res, nums[mid]) 
            
            if nums[mid] >= nums[l]: # It means that m is a part of the left portion and we have to search the right part
                l = mid + 1 # Search the right side
            else:
                # m may be in the right side so we have to search the left side
                r = mid - 1
        return res