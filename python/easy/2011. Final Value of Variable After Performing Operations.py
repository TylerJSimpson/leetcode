class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        addition_one = operations.count('X++')
        addition_two = operations.count('++X')
        subtraction_one = operations.count('X--')
        subtraction_two = operations.count('--X')
        final_value = addition_one + addition_two - subtraction_one - subtraction_two
        return final_value
