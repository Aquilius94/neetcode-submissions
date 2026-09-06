class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset:set = set(nums)

        return len(numset) != len(nums)
        