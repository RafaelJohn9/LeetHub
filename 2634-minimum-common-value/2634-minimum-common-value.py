class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        def is_num_in_arr(num: int, arr: List[int]):
            for arr_num in arr:
                if arr_num == num:
                    return True
                elif arr_num > num:
                    return False
            
            return False
        

        for num in nums1:
            if is_num_in_arr(num, nums2):
                return num
        
        return -1