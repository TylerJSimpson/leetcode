class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_forward = str(x)
        str_backward = str_forward[::-1]
        return str_forward == str_backward
