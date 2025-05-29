class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_longest(s: str, word: str) -> bool:
            i = 0
            j = 0

            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                
                i += 1
            
            return len(word) == j
        
        best = ""
        for word in dictionary:
            if is_longest(s, word):
                if len(word) > len(best) or (len(word) == len(best) and word < best):
                    best = word
        return best