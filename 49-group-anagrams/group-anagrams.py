class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            brokenString = list(string)
            brokenString.sort()
            key = str(brokenString)

            
            value = anagrams.get(key, None)

            if value is None:
                anagrams[key] = [string]
            else:
                anagrams[key].append(string)
        
        listOfAnagrams = [value for value in anagrams.values()]
        return listOfAnagrams