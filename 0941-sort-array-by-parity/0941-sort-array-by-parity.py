class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        response = []

        for num in nums:
            if num % 2 == 0:
                response.insert(0, num)
            else:
                response.append(num)
                
        return response