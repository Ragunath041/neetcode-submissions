class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        i = 0
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target and i != j:
                    res.append(i)
                    res.append(j)
                j += 1
            i += 1
        return res