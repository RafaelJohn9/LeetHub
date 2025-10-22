class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0 :
            return ""

        prefix=strs[0]

        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix =prefix[:-1]

                if not prefix :
                    return ""

        return prefix

