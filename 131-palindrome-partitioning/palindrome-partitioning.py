class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(s: str):
            return s == s[::-1]

        def backtrack(start, path, res, s):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                if isPalindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end, path, res, s)
                    path.pop()

        backtrack(0, [], res, s)
        return res
