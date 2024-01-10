/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    for (let i = 0; i < nums.length; i++){
        if (nums[i] == 0){
            let j = i + 1;
            while (j < nums.length){
                if (nums[j] !== 0){
                    let temp = nums[j];
                    nums[j] = 0;
                    nums[i] = temp;
                    break;
                }
                j++;
            }
        }
    }
    return nums;
};