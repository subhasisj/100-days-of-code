class Solution:
    def isValid(self, s: str) -> bool:
        open_close_map = {
            "(": ")",
            "{":"}",
            "[":"]"
        }
        stack = []
        
        for i in s:
            if (stack and open_close_map.get(stack[-1])==i):
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0