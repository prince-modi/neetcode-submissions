impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32,i32> = HashMap::new();

        for i in 0..nums.len(){
            let comp = target - nums[i];
            if map.contains_key(&comp){
                return vec![map[&comp], i as i32]
            }
            *map.entry(nums[i]).or_insert(0) =i as i32;
        }
        unreachable!()
    }
}
