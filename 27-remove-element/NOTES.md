while ind < len(nums):
if nums[ind] == val
nums.remove(ind) # Remove the first matching element
return len(nums)
or
def removeElement(self, nums: List[int], val: int) -> int:
k=0
for left in range(len(nums)):
if nums[left] != val:
nums[k] = nums[left]
k+=1
return k