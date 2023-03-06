class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
    """
    numJewelsInStone counts the number of jewels that are also stones
    jewels: string (only english letters, all characters unique, 1 <= jewels.length)
    stones: string (only english letters, stones.length <= 50)
    """
        jewels_list = list(jewels)
        stones_list = list(stones)
        jewel_count = 0
        for stone in stones_list:
            if stone in jewels_list:
                jewel_count += 1
        return jewel_count
