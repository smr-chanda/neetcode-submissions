class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        nums = list(set_nums)
        if len(set_nums) == 0 or len(set_nums) == 1:
            return len(set_nums)

        max_k = 1
        for i in range(len(set_nums)):

            n = nums[i]

            if n not in set_nums:
                continue

            k = 1
            while n - 1 in set_nums:
                k += 1
                set_nums.remove(n - 1)
                n -= 1

            n = nums[i]
            while n + 1 in set_nums:
                k += 1
                set_nums.remove(n + 1)
                n += 1
            
            if k > max_k:
                max_k = k

        return max_k