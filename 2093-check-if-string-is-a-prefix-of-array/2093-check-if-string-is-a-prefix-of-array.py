class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        """
        checks if s is a prefix to the first k  words
        """

        words_prefix: str = ""
        n_s: int = len(s)
        n_words:int = len(words)
        i: int = 0

        while len(words_prefix) < n_s and i < n_words:
            words_prefix += words[i]
            i += 1
        
        return words_prefix == s
