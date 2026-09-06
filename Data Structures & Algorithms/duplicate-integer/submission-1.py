class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen:dict = {}

        for idx, num in enumerate(nums):
            if num in seen:
                return True
            seen[num] = idx
        return False
        