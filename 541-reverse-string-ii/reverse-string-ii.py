class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)

        for i in range(0, len(s), k * 2):
            s_list[i: i + k] = reversed(s_list[i: i + k])
        
        return "".join(s_list)