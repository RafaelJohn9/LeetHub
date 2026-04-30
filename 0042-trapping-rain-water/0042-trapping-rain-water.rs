impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        // 1. initialize the variables
        // left, right, left_max, right_max, trapped_water
        // 2. Begin the loop,
        // 3. Check which is smaller height[left], height[right]
        // 4. if height[left], check if the bar is bigger than  or equal to the curr left_max, then assign
        // left max to it.
        // 5. Else find the trap water.
        // 6. Do the same to right condition
        // 7. Return the trapped_water

        let mut left = 0;
        let mut right = height.len() - 1;
        let mut left_max = 0;
        let mut right_max = 0;
        let mut trapped_water = 0;

        while (left < right){
            if (height[left] < height[right]){
                if (height[left] >= left_max){
                    left_max = height[left];
                }else{
                    trapped_water += left_max - height[left]
                }
                left += 1;
            }
            else {
                if (height[right] >= right_max){
                    right_max = height[right];
                }else{
                    trapped_water += right_max - height[right]
                }
                right -= 1;
            }
        }

        trapped_water
    }
}