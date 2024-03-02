/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let left = 0;
    let right = nums.length - 1;

    if (nums.length === 2){
        let count = nums.reduce((count, element) => (element === val ? count + 1: count), 0);
        if (count === 2){
            return (0);
        }else if (count === 1){
            if (nums[0] === val){
                nums[0] = nums[1];
            }
            return (1);
        }else{
            return (2);
        }
    }
    
    while(left < right){
        if (nums[left] === val){
            if (nums[right] === val){
                right--;
                continue;
            }
            let temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            right--;
        }
        left++;
    }
    if (left === right && nums[left] === val){
        left--;
    }
    return nums[left] !== val ? left + 1 : left;
};