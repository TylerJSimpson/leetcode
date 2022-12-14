class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_list = list(jewels)
        stones_list = list(stones)
        jewel_count = 0
        for stone in stones_list:
            if stone in jewels_list:
                jewel_count += 1
        return jewel_count
