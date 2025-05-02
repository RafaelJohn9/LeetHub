class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Reorder nums into a wiggle sort pattern:
        nums[0] < nums[1] > nums[2] < nums[3] ...
        Modify nums in-place.
        """

        n = len(nums)
        if n <= 1:
            return

        # Step 1: Find the median
        sorted_nums = sorted(nums)
        median = sorted_nums[n // 2]

        # Step 2: Index mapping
        def index(i: int) -> int:
            return (1 + 2 * i) % (n | 1)

        # Step 3: 3-way partition using virtual indexing
        left, i, right = 0, 0, n - 1
        while i <= right:
            mapped_i = index(i)
            if nums[mapped_i] > median:
                nums[index(left)], nums[mapped_i] = nums[mapped_i], nums[index(left)]
                left += 1
                i += 1
            elif nums[mapped_i] < median:
                nums[index(right)], nums[mapped_i] = nums[mapped_i], nums[index(right)]
                right -= 1
            else:
                i += 1
