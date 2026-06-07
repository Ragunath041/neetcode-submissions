class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            if not (i - 1) in nums:
                l = 0
                while(i + l) in nums:
                    l += 1
                res = max(res , l)
        return res