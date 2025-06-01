class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}

        n = len(s2)
        i = 0

        # Map all s1 characters in a dict
        for char in s1:
            s1_dict[char] = s1_dict.get(char, 0) + 1
        
        temp_dict = s1_dict.copy()

        while i < n:
            temp_i = i
            while temp_i < n and temp_dict.get(s2[temp_i], 0) > 0 :
                temp_dict[s2[temp_i]] -= 1
                temp_i += 1
            else:
                i += 1

            if not any(list(temp_dict.values())):
                return True
            
            temp_dict = s1_dict.copy()
        
        return False