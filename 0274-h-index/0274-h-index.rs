impl Solution {
    pub fn h_index(mut citations: Vec<i32>) -> i32 {
        citations.sort_by(|a, b| b.cmp(a));

        for i in 0..=citations.len() - 1{
            if (citations[i] < ((i + 1) as i32)){
                return i as i32;
            }
        }
        return citations.len() as i32
    }
}