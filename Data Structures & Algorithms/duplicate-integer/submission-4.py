class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = set(nums)
        if sorted(nums) == sorted(list(dupe)):
            return False
        else:
            return True
         