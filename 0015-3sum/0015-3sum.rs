impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        // 1. Sort the array
        // 2. initialize n (length of the array)
        // 3. initialize result, the result array
        // 4. Begin the for loop that will be used to iterate the fixed pointer
        // 5. Check if the fixed pointer matches with the previous fixed pointer if not 0
        // 6. Begin while loop (left <  right) to check for sum equaling to 0
        // 7. if sum equals 0 add to result. iterate left and right checking for non duplicate values
        // 8. if sum is greater than 0, decrease right
        // 9. Else increase left, return result

        nums.sort();
        let n = nums.len();
        let mut result = Vec::new();

        for i in 0..n{
            if i > 0 && nums[i] == nums[i - 1]{
                continue;
            }

            let mut left = i + 1;
            let mut right = n - 1;

            while left < right{
                let sum = nums[i] + nums[left] + nums[right];

                if (sum == 0){
                    result.push(vec![nums[i], nums[left], nums[right]]);

                    while left < right && nums[left] == nums[left + 1]{
                        left += 1;
                    }

                    while left < right && nums[right] == nums[right - 1]{
                        right -= 1;
                    }

                    left += 1;
                    right -= 1;
                }
                else if (sum < 0){
                    left += 1
                }
                else{
                    right -= 1
                }
            }
        }
        result
    }
}