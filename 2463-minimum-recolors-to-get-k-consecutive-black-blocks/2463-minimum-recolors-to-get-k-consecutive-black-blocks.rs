impl Solution {
    pub fn minimum_recolors(blocks: String, k: i32) -> i32 {
        let mut ops = 0;
        let chars: Vec<char> = blocks.chars().collect();

        for i in 0..k{
            if (chars[i as usize] == 'W'){
                ops += 1;
            }
        }
        let mut temp = ops;

        for i in k..(chars.len() as i32){
            let to_be_removed_index = i - k;

            if (chars[to_be_removed_index as usize] == 'W'){
                temp -= 1;
            }

            if (chars[i as usize] == 'W'){
                temp += 1;
            }

            if (ops > temp){
                ops = temp;
            }
        }

        ops
    }
}