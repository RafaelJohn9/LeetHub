class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0
        good_integer = ""
        while i < len(num) - 2:
            if num[i] == num[i + 1] and num[i] == num[i + 2]:
                if len(good_integer) > 0:
                    good_integer = str(max(int(good_integer), int(num[i])))
                else:
                    good_integer = num[i]
                i += 3
            else:
                i += 1
        return (good_integer * 3)
        