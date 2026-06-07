class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def counting(str):
            freq_counter = {}
            for i in str:
                freq_counter[i] = freq_counter.get(i , 0) + 1
            return freq_counter
        print(counting(s) , counting(t))
        return counting(s) == counting(t)
        