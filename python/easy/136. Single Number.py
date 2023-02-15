class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    """
    singleNumber takes nums List[int] and finds the singular element that is not duplicated and returns it
    nums List[int] (each element appears twice except for 1)
        (1 <= nums.length <= 3 * 104)
        (-3 * 104 <= nums[i] <= 3 * 104)
    """
        ts_set = set()
        for i in nums:
            if i in ts_set:
                ts_set.remove(i)
            else:
                ts_set.add(i)
        return list(ts_set)[0]
