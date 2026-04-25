impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map: HashMap<Vec<i32>,Vec<String>> = HashMap::new();

        for string in strs{
            let mut key: Vec<i32> = vec![0;26];
            for c in string.chars(){
                let idx = c as usize - 'a' as usize;
                key[idx]+=1;
            }
            map.entry(key).or_default().push(string);
        }
        map.into_values().collect()
    }
}
