class Solution:
    def isPalindrome(self, x: int) -> bool:
    """
    isPalindrome returns true or false depending on if x int input is a palindrome number
    palindrome numbers are the same forward as they are backwards
    x: int (-231 <= x <= 231 - 1)
    """
        str_forward = str(x)                            #convert x int to str
        str_backward = str_forward[::-1]                #reverse str
        return str_forward == str_backward              #return comparison of forward and backwards str
