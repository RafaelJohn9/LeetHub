/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if (nums.length === 1){
        return nums;
    }

    let i = 0;
    while (i < nums.length){
        if (i === 0){
            i++;
        }
        if (nums[i - 1] === nums[i]){
            nums.splice(i, 1)
        }
        else{
            i++;
        }
    }
    return nums.length
};