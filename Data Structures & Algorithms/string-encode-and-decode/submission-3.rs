impl Solution {
    pub fn encode(strs: Vec<String>) -> String {
        let mut encoded = String::new();
        for string in strs.iter(){
            let prefix = format!("{}#", string.len());
            encoded.push_str(&prefix);
            encoded.push_str(&string);
        }
        encoded

    }

    pub fn decode(s: String) -> Vec<String> {
        let mut res: Vec<String> = Vec::new();
        let bytes = s.as_bytes();
        let mut i = 0;
        while i<bytes.len(){
            let mut j = i;
            while bytes[j]!=b'#'{
                j+=1;
            }
            let length:usize = s[i..j].parse().unwrap();
            i=j+1;
            j=i+length;
            res.push(s[i..j].to_string());
            i=j;
        }
        res

    }
}
