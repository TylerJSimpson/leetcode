class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
    """
    finalValueAfterOperations returns the same when given 4 increment and decrement possibilities in list operations.
    ++X and X++ increments, --X and X-- decrements, X begins at 0
    """
        addition_one = operations.count('X++')
        addition_two = operations.count('++X')
        subtraction_one = operations.count('X--')
        subtraction_two = operations.count('--X')
        final_value = addition_one + addition_two - subtraction_one - subtraction_two
        return final_value
