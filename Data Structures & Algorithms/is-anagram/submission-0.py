class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        seen:dict[str, int] = {}

        for ch in s:
            if ch in seen:
                seen[ch] += 1
            else:
                seen[ch] = 1
        
        seenT:dict[str, int] = {}

        for ch in t: 
            if ch in seenT:
                seenT[ch] += 1
            else: seenT[ch] = 1

        for ch in seen:
            if seen[ch] != seenT.get(ch, 0):
                return False
        return True
