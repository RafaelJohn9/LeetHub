class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums =  nums
        self.k = k

    
    def is_kth_largest(self):
        self.nums.sort(reverse=True)

        prev = self.nums[0]
        return self.nums[self.k - 1]

        

    def add(self, val: int) -> int:
        self.nums.append(val)
        return self.is_kth_largest()


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)