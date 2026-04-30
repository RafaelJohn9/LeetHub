impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut result = vec![1; n];
        

        // prefix pass
        let mut left = 1;
        for i in 0..n{
            result[i] = left;
            left *= nums[i];
        }

        // suffix pass
        let mut right = 1;
        for i in (0..n).rev(){
            result[i] *= right;
            right *= nums[i];
        }

        result
    }
}