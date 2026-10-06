class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums:dict = {}
        diff:None | int = None 

        for i, value in enumerate(nums):
            difference = target - nums[i]

            if difference in seen_nums:
                return [seen_nums[difference], i]
            else:
                seen_nums[value] = i

        return [-1, -1]
        