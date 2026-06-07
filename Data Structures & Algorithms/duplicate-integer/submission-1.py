class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_counter = {}
        flag = False
        for i in nums:
            freq_counter[i] = freq_counter.get(i , 0) + 1
        for i in freq_counter.values():
            if i >= 2:
                flag = True
                break
        return flag