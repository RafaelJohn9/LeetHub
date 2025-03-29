class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        key_list = []
        i = 0

        while i < n:
            if key == nums[i]:
                key_list.append(i)
            i += 1

        prev_key = None
        count = 0
        next_key =  key_list[count]

        result = []
        i = 0
        while i < n:
            if nums[i] == key:
                result.append(i)
                prev_key = next_key
                count = count + 1 if  count + 1 < len(key_list) else count
                next_key = key_list[count]
            elif isinstance(prev_key, int) and  abs(i - prev_key) <= k:
                result.append(i)
            elif abs(i - next_key) <= k:
                result.append(i)
            
            i += 1
        
        return result
