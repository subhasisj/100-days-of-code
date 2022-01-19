from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s)) #sorted on a string converts to a list, we need to join to make it again string 
            group[sorted_s].append(s)
        return group.values()