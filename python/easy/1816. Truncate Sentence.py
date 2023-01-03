class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        truncated_string = ''
        count = 0
        for char in s:
            if char == ' ':
                count += 1
            if count == k:
                break
            truncated_string += char
        return truncated_string
