impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = height.len().saturating_sub(1);
        let mut max_area = 0;

        while (left < right){
            let mut min_height_index = 0;

            if (height[left] < height[right]){
                min_height_index = left;
            }
            else{
                min_height_index = right;
            }

            let current_area = height[min_height_index] * (right - left) as i32;

            if (max_area < current_area){
                max_area =  current_area;
            }

            if (min_height_index == left){
                left += 1;
            }
            else{
                right -= 1;
            }
        }
        return max_area;
    }
}