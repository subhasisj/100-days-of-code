class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1.isnumeric():
            return
        if not num2.isnumeric():
            return
        
        num1,num2 = int(num1),int(num2)
        
        return str(num1*num2)
        