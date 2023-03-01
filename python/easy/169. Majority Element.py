class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    """
    majorityElement returns the element of array nums that appears more than [n / 2] times
    nums array (n == nums.length) (1 <= n <= 5 * 104) (-109 <= nums[i] <= 109)
    """
        nums_dict = {}                                                  #create empty dict
        for number in nums:
            nums_dict.setdefault(number,0)                              #add number in nums to dict set value to 0
            nums_dict[number] += 1                                      #increment value by 1 for each occurrence of nums
        max_number = max(nums_dict, key = lambda x: nums_dict[x])       #get key with value of highest increment
        return max_number
