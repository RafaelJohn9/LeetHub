class Solution:
    def countTriplets(self, arr: List[int]) -> int:
         n = len(arr)
         prefix = [0] * n
         
         # Compute the prefix XOR
         prefix[0] = arr[0]
         for i in range(1, n):
             prefix[i] = prefix[i-1] ^ arr[i]
    
         count = 0
         for i in range(n):
             for k in range(i+1, n):
                 if prefix[k] == (prefix[i-1] if i > 0 else 0):
                     count += (k - i)  # Number of valid j's between i and k

         return count