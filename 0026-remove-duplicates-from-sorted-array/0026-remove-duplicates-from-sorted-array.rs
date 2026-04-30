impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut slow = 0;
        let n = nums.len();
        
        for fast in 1..n{
            if (nums[slow] != nums[fast]){
                slow += 1;
                nums[slow] = nums[fast]
            }
        }

        (slow + 1) as i32
    }
}