class Solution:
    def reverse(self, x: int) -> int:
        print('x:',x)
        print('str(-1*x)',str(-1*x)[::-1])
        reverse_x  = str(x)[::-1] if x > 0 else str(abs(x))[::-1]
        final_num = '-'+ reverse_x if x < 0 else reverse_x
        final_num = int(final_num)
        if final_num in range((-2)**31, 2**31-1):
            return final_num
        return 0
        
        
