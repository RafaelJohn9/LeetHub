/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    let numList = nums.slice(0, k);
    let sum = numList.reduce((accumulator, element) => accumulator + element, 0);
    let max = sum;

    for (let i = k; i < nums.length; i++) {
        sum = sum - nums[i - k] + nums[i];
        max = Math.max(max, sum);
    }

    return max / k;
};