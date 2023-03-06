class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        moveZeroes arranges list nums so that all 0s are at the end.
        """
        for i in nums:
            if i == 0:
                nums.append(0)
                nums.remove(i)
            
