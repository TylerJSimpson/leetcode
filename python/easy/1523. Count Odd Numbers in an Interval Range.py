class Solution(object):
    def countOdds(self, low, high):
    """
    countOdds takes low (int) and high (int) as inputs and returns the count of odd numbers within the range
    low: int
    high: int
    0 <= low <= high <= 10^9
    """
        if low % 2 == 1 or high % 2 == 1:
          return (high-low) / 2 + 1                 #if low or high are odd divide difference by 2 and add 1
        else:
          return (high-low) / 2                     #if low and high are even divide difference by 2
