class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def next_index(i: int) -> int:
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow, fast = i, i
            direction = nums[i] > 0

            while True:
                next_slow = next_index(slow)
                next_fast = next_index(fast)
                if nums[fast] * nums[next_fast] <= 0:
                    break
                next_fast = next_index(next_fast)
                if nums[fast] * nums[next_fast] <= 0:
                    break

                slow = next_index(slow)
                fast = next_fast

                if slow == fast:
                    if slow == next_index(slow):  # One-element loop
                        break
                    return True

            # Mark path as visited
            j = i
            while nums[j] * nums[next_index(j)] > 0:
                temp = j
                j = next_index(j)
                nums[temp] = 0

        return False
