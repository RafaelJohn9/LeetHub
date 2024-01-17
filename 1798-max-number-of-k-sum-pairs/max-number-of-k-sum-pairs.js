/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    let frequency = {};
    let numberOfOperations = 0;

    for (const num of nums) {
        const rem = k - num;

        if (frequency[rem] && frequency[rem] > 0) {
            // Found a matching pair
            numberOfOperations++;
            frequency[rem]--;
        } else {
            // Update frequency of current element
            frequency[num] = (frequency[num] || 0) + 1;
        }
    }

    return numberOfOperations;
};
