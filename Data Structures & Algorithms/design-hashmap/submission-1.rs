struct MyHashMap {
    set: Vec<bool>,
    values: Vec<i32>
}

impl MyHashMap {
    pub fn new() -> Self {
        Self { set : vec![false; 1000001],
        values: vec![0; 1000001]}
    }

    pub fn put(&mut self, key: i32, value: i32) {
        self.set[key as usize]=true;
        self.values[key as usize]=value;

    }

    pub fn get(&self, key: i32) -> i32 {
        if !self.set[key as usize]{
            return -1
        }
        self.values[key as usize]

    }

    pub fn remove(&mut self, key: i32) {
        self.set[key as usize]=false

    }
}
