impl Solution {
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        if (k == 0 || nums.len() <= 1){
            return;
        }

        let n = nums.len();
        let valid_k = k as usize % n ;

        nums.reverse();
        nums[..valid_k].reverse();
        nums[valid_k..].reverse();
    }
}