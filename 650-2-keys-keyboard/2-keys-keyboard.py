class Solution:
    def minSteps(self, n: int) -> int:
        if not isinstance(n, int):
            return 0
            
        string = "H"
        copy = lambda src: src
        paste = lambda string1, string2: string1 + string2
        numberOfOperations = 0
        
        while len(string) < n:
            if n % len(string) == 0:
                strCopied = copy(string)
                string = paste(strCopied, string)
                numberOfOperations += 2
            else:
                string = paste(strCopied, string)
                numberOfOperations += 1
        return numberOfOperations
