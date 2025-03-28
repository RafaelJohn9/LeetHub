class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        n = len(words)
        i = 0
        n_word = len(searchWord)

        while i < n:
            if words[i].startswith(searchWord):
                return i + 1

            i += 1
        
        return -1