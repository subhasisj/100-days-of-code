class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        check = {}
        for i in range(len(numbers)):
            required = target - numbers[i]
            if required in check:
                return [check[required]+1,i+1]
            else:
                check[numbers[i]] = i
        
            