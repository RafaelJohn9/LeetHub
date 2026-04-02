/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
 use std::collections::HashMap;
 use rand::Rng;

 struct RandomizedSet {
    set: HashMap<i32, i32>,
 }

impl RandomizedSet {

    fn new() -> Self {
        Self{
            set: HashMap::new(),
        }
    }
    
    fn insert(&mut self, val: i32) -> bool {
        if (self.set.contains_key(&val)){
            return false;
        }
        self.set.insert(val, val);
        return true;
    }
    
    fn remove(&mut self, val: i32) -> bool {
        if (self.set.contains_key(&val)){
            self.set.remove(&val);
            return true;
        }
        return false
    }
    
    fn get_random(&self) -> i32 {
        let map_len = self.set.len();
        let mut rng = rand::thread_rng();
        let rand_num = rng.gen_range(0..map_len);

        let map_keys: Vec<&i32> = self.set.keys().collect();
        let key = map_keys[rand_num];

        return *self.set.get(key).unwrap();
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */