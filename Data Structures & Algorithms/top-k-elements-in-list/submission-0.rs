impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let bucket_size = nums.len()+1;
        let mut bucket: Vec<Vec<i32>> = vec![Vec::new(); bucket_size];
        let mut counts: HashMap<i32, usize> = HashMap::new();
        let mut ans: Vec<i32> = Vec::new();
        for num in nums{
            *counts.entry(num).or_insert(0)+=1;
        }

        for (key,count) in counts.iter(){
            bucket[*count as usize].push(*key);
        }

        for b in bucket.iter().rev(){
            for element in b.iter(){
                if ans.len()<k as usize{
                    ans.push(*element);
                } else {
                    break;
                }
            }
        }
        ans



    }
}
