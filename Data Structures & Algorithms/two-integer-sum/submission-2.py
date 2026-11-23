class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}

        for i, num in enumerate(nums):
            second_num = target - num
            if second_num in dict_nums:
                return [dict_nums[second_num], i]
            dict_nums[num] = i
        return