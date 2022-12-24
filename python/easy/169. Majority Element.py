class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}
        for number in nums:
            nums_dict.setdefault(number,0)
            nums_dict[number] += 1
        max_number = max(nums_dict, key = lambda x: nums_dict[x])
        return max_number
