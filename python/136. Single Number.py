class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ts_set = set()
        for i in nums:
            if i in ts_set:
                ts_set.remove(i)
            else:
                ts_set.add(i)
        return list(ts_set)[0]
