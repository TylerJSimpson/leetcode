class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
    '''
    getConcatenation takes an input array nums and concatenates it with itself
    nums: int array (n == nums.length, 1 <= n <= 1000, 1 <= nums[i] <= 1000)
    '''
        nums_length = len(nums) * 2                 #double the length of array nums
        nums_concat = []
        while len(nums_concat) < nums_length:       #iterate through array nums twice
            for i in range(len(nums)):              #add each character to new array
                nums_concat.append(nums[i])
        return nums_concat
