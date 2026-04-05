impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
           let mut counter = 0;
           let mut majority_element = 0;

           for element in nums.iter(){
            if (counter == 0){
                counter += 1;
                majority_element = *element;
            }
            else if (majority_element != *element){
                counter -= 1;
            }
            else{
                counter += 1;
            }
           }
           return majority_element;
    }
}