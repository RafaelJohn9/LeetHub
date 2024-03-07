/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    // Sort the array in ascending order
    nums.sort((a, b) => a - b);

    let closestSum = nums[0] + nums[1] + nums[2]; // Initialize closest sum

    for (let i = 0; i < nums.length - 2; i++) {
        let left = i + 1;
        let right = nums.length - 1;

        while (left < right) {
            let sum = nums[i] + nums[left] + nums[right];

            // Update closest sum if the current sum is closer to target
            if (Math.abs(sum - target) < Math.abs(closestSum - target)) {
                closestSum = sum;
            }

            if (sum < target) {
                left++; // Move left pointer to increase sum
            } else if (sum > target) {
                right--; // Move right pointer to decrease sum
            } else {
                return closestSum; // If sum equals target, return immediately
            }
        }
    }

    return closestSum;
};
