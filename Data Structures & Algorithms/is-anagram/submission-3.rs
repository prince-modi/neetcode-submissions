impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut s_key: Vec<u32> = vec![0; 26];
        let mut t_key: Vec<u32> = vec![0; 26];

        for c in s.chars(){
            let idx = c as usize - 'a' as usize;
            s_key[idx] += 1;
        }
        for t in t.chars(){
            let idx = t as usize - 'a' as usize;
            t_key[idx] += 1;
        }
        s_key == t_key
    }
}
