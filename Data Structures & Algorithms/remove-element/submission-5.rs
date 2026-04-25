impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut n = 0;
        let mut k = 0;
        while n<nums.len(){
            if nums[n]!=val{
                nums[k]=nums[n];
                k+=1;
            }
            n+=1;
        }
        k as i32

    }
}
