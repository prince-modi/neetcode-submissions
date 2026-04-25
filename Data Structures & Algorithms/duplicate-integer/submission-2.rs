impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let set: HashSet<i32> = HashSet::from_iter(nums.iter().copied());
        nums.len()!=set.len()
    }
}
