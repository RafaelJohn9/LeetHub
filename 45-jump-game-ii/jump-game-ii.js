/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let numsLength = nums.length;

    if (numsLength < 2) {
        return 0; // No jumps needed if already at the end or no elements
    }

    let steps = 0;
    let maxReach = 0;
    let lastJumpEnd = 0;

    for (let i = 0; i < numsLength - 1; i++) {
        maxReach = Math.max(maxReach, i + nums[i]);

        if (i === lastJumpEnd) {
            lastJumpEnd = maxReach;
            steps++;
        }
    }

    return steps;
};