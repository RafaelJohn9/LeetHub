class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        list_of_c = [i for i in range(len(s)) if s[i] == c]

        result = []
        for i in range(len(s)):
            result.append(min([abs(i - index_of_c) for index_of_c in list_of_c]))
        
        return result