class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_length = len(nums) * 2
        nums_concat = []
        while len(nums_concat) < nums_length:
            for i in range(len(nums)):
                nums_concat.append(nums[i])
        return nums_concat
