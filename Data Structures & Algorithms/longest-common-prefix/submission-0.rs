impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut prefix = strs[0].as_str();
        for i in 1..strs.len(){
            let s = strs[i].as_str();
            let len = min(prefix.len(),s.len());
            let mut j = 0;
            while j<len && s.as_bytes()[j] == prefix.as_bytes()[j]{
                j+=1;
            }
            prefix=&prefix[..j];
        }
        prefix.to_string()

    }
}
