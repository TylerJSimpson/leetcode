class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
    '''
    truncateSentence takes input string s and includes only the first k (int) words
    s: str (only lowercase and uppercase English letters and spaces, 1 <= s.length <= 500, words separated only by a single space, no leading/trailing spaces)
    k: int (range [1, number of words in s])
    '''
        truncated_string = ''               #create empty string truncated_string
        count = 0
        for char in s:                      #iterate thru characters in string
            if char == ' ':                 #if character is a space increase counter
                count += 1
            if count == k:                  #once count = k break the loop
                break
            truncated_string += char        #add character to truncated_string
        return truncated_string
