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
        
        dictionary.sort(key=len, reverse=True)

        result_list = []
        
        i = 0
        n = len(dictionary)

        while i < n:
            if len(result_list) > 0 and len(result_list[-1]) > len(dictionary[i]):
                return min(result_list)
            elif is_longest(s, dictionary[i]):
                result_list.append(dictionary[i])

            i += 1
        
        return min(result_list) if len(result_list) > 0 else ""