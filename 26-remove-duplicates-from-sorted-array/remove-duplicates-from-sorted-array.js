/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let i = 0;
    if (nums.length <= 1){
        return nums.length
    }

    while (i < nums.length){
        if (i === 0){
            i++;
            continue;
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