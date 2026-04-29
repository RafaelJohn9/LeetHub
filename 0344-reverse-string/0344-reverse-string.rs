impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
       let mut left: usize = 0;
       let mut right: usize = s.len() - 1;

       while (left < right){
        let temp = s[left];
        s[left] = s[right];
        s[right] =  temp;

        left += 1;
        right -= 1;
       }
    }
}