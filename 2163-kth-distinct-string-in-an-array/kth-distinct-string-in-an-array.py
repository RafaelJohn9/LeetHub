class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        """
        finds the kth distinct element
        """
        mem: Dict[str, int] = {}

        for string in arr:
            if not mem.get(string, False):
                mem[string] = 1
            elif mem.get(string) == 1:
                mem[string] += 1
            else:
                mem[string] += 1

        count: int = 0
        for key, value in mem.items():
            if value == 1:
                count += 1

            if count == k:
                return key
    
        return ""