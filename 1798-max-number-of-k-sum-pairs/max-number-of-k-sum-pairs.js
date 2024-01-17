/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
     let i = 0;
     let numberOfOperations = 0;
     while (i < nums.length){
         const value = nums[i]
         const rem = k - value;
         if (rem < 0){
             i++;
             continue;
         }
         let left = i;
         let right = nums.length - 1
         while (left < right){
             if (nums[right] ===  rem){
                 nums.splice(right, 1);
                 nums.splice(left, 1);
                 numberOfOperations++;
                 break;
             }
             right--;
         }
         if (left >= right){
             i++;
         }
     }
     return  numberOfOperations
};