use std::collections::HashMap;
use rand::Rng;

struct RandomizedSet {
    vals: Vec<i32>,
    indices: HashMap<i32, usize>,
}

impl RandomizedSet {

    fn new() -> Self {
        Self {
            vals: Vec::new(),
            indices: HashMap::new(),
        }
    }
    
    fn insert(&mut self, val: i32) -> bool {
        if self.indices.contains_key(&val) {
            return false;
        }

        self.vals.push(val);
        self.indices.insert(val, self.vals.len() - 1);
        true
    }
    
    fn remove(&mut self, val: i32) -> bool {
        if let Some(&idx) = self.indices.get(&val) {
            let last = *self.vals.last().unwrap();

            // Move last element into idx
            self.vals[idx] = last;
            self.indices.insert(last, idx);

            // Remove last element
            self.vals.pop();
            self.indices.remove(&val);

            true
        } else {
            false
        }
    }
    
    fn get_random(&self) -> i32 {
        let mut rng = rand::thread_rng();
        let idx = rng.gen_range(0..self.vals.len());
        self.vals[idx]
    }
}